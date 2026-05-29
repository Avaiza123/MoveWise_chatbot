import json
import re
import time
from difflib import SequenceMatcher
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class KnowledgeEntry:
    key: str
    question: str
    answer: str
    source: str
    confidence: float
    tags: List[str]
    intent: str
    updated_at: float


class KnowledgeStore:
    """Simple persistent knowledge memory with lexical retrieval."""

    STOPWORDS = {
        "a", "an", "and", "are", "as", "at", "be", "but", "by", "do", "for", "from",
        "get", "got", "how", "i", "if", "in", "is", "it", "me", "my", "need", "of",
        "on", "or", "our", "should", "some", "that", "the", "their", "them", "there",
        "these", "they", "this", "to", "too", "was", "we", "what", "when", "where",
        "who", "why", "will", "with", "you", "your", "much", "many", "need", "want",
        "please", "tell", "about", "can", "could", "would", "doe", "did", "does",
    }

    GENERIC_ANSWER_MARKERS = (
        "simple fitness guide",
        "simple diet guide",
        "food information available",
        "daily wellness tips",
        "if you want, i can",
    )

    def __init__(self, file_path: Optional[Path] = None):
        default_path = Path(__file__).resolve().parent / "knowledge_memory.json"
        self.file_path = file_path or default_path
        self.entries: Dict[str, KnowledgeEntry] = {}
        self._load()

    def _tokenize(self, text: str) -> List[str]:
        tokens = re.findall(r"\b[a-z0-9]+\b", (text or "").lower())
        return [token for token in tokens if token not in self.STOPWORDS]

    def _load(self) -> None:
        try:
            if not self.file_path.exists():
                self.entries = {}
                return
            payload = json.loads(self.file_path.read_text(encoding="utf-8"))
            if not isinstance(payload, list):
                self.entries = {}
                return
            loaded: Dict[str, KnowledgeEntry] = {}
            for item in payload:
                if not isinstance(item, dict):
                    continue
                try:
                    entry = KnowledgeEntry(
                        key=item["key"],
                        question=item["question"],
                        answer=item["answer"],
                        source=item.get("source", "local"),
                        confidence=float(item.get("confidence", 0.6)),
                        tags=item.get("tags", []),
                        intent=item.get("intent", "unknown"),
                        updated_at=float(item.get("updated_at", time.time())),
                    )
                    loaded[entry.key] = entry
                except Exception:
                    continue
            self.entries = loaded
        except Exception:
            self.entries = {}

    def _save(self) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        payload = [asdict(entry) for entry in self.entries.values()]
        self.file_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")

    def add_or_update(
        self,
        key: str,
        question: str,
        answer: str,
        source: str = "local",
        confidence: float = 0.7,
        intent: str = "unknown",
        tags: Optional[List[str]] = None,
    ) -> None:
        if not key or not answer:
            return
        now = time.time()
        entry = KnowledgeEntry(
            key=key.strip().lower(),
            question=question.strip(),
            answer=answer.strip(),
            source=source,
            confidence=max(0.0, min(confidence, 1.0)),
            tags=tags or [],
            intent=(intent or "unknown").strip().lower(),
            updated_at=now,
        )
        self.entries[entry.key] = entry
        self._save()

    def _is_generic_answer(self, text: str) -> bool:
        lowered = (text or "").lower().strip()
        if not lowered:
            return True
        return any(marker in lowered for marker in self.GENERIC_ANSWER_MARKERS)

    def retrieve(self, query: str, intent: Optional[str] = None, min_score: float = 0.45) -> Optional[Dict]:
        query_tokens = set(self._tokenize(query))
        if not query_tokens:
            return None

        best_entry = None
        best_score = 0.0
        intent_norm = (intent or "unknown").strip().lower()

        for entry in self.entries.values():
            if self._is_generic_answer(entry.answer):
                continue

            if intent_norm != "unknown" and entry.intent not in {intent_norm, "unknown"}:
                continue

            if entry.confidence < 0.35:
                continue

            candidate_tokens = set(self._tokenize(entry.question)) | set(self._tokenize(" ".join(entry.tags)))
            if not candidate_tokens:
                continue

            overlap = len(query_tokens & candidate_tokens)
            union = len(query_tokens | candidate_tokens)
            jaccard = overlap / union if union else 0.0

            seq = SequenceMatcher(None, (query or "").lower(), (entry.question or "").lower()).ratio()
            blended = (jaccard * 0.75) + (seq * 0.25)

            if intent_norm != "unknown" and entry.intent == intent_norm:
                blended += 0.08

            if blended > best_score:
                best_score = blended
                best_entry = entry

        if not best_entry or best_score < min_score:
            return None

        return {
            "answer": best_entry.answer,
            "source": best_entry.source,
            "confidence": best_entry.confidence,
            "retrieval_score": round(best_score, 3),
            "key": best_entry.key,
            "tags": best_entry.tags,
            "intent": best_entry.intent,
        }

    def ingest_web_cache(self, web_cache: Dict[str, Dict[str, str]]) -> int:
        if not isinstance(web_cache, dict):
            return 0

        count = 0
        for key, value in web_cache.items():
            if not isinstance(value, dict):
                continue
            summary = (value.get("summary") or "").strip()
            if not summary:
                continue

            source_url = (value.get("source_url") or "").strip()
            title = (value.get("title") or "web knowledge").strip()
            answer = f"{summary}\n\nSource: {source_url}" if source_url else summary
            tags = [t for t in self._tokenize(title)[:6]]

            self.entries[key] = KnowledgeEntry(
                key=key,
                question=key,
                answer=answer,
                source="web_cache",
                confidence=0.6,
                tags=tags,
                intent=(key.split("::", 1)[0] if "::" in key else "unknown"),
                updated_at=time.time(),
            )
            count += 1

        if count:
            self._save()
        return count

    def stats(self) -> Dict[str, int]:
        by_source: Dict[str, int] = {}
        for entry in self.entries.values():
            by_source[entry.source] = by_source.get(entry.source, 0) + 1
        return {
            "total_entries": len(self.entries),
            **{f"source_{k}": v for k, v in by_source.items()},
        }

    def prune_low_quality(self) -> int:
        """Remove generic/low-confidence entries from persistent memory."""
        to_delete = []
        for key, entry in self.entries.items():
            if entry.confidence < 0.2:
                to_delete.append(key)
                continue
            if self._is_generic_answer(entry.answer):
                to_delete.append(key)
                continue

        for key in to_delete:
            self.entries.pop(key, None)

        if to_delete:
            self._save()
        return len(to_delete)

# Response Models
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

class ResponseType(Enum):
    SUCCESS = "success"
    ERROR = "error"
    INFO = "info"
    WARNING = "warning"

@dataclass
class ChatbotResponse:
    """Standard response format for all chatbot endpoints"""
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    response_type: ResponseType = ResponseType.SUCCESS
    error_code: Optional[str] = None

    def _resolve_answer_source(self) -> str:
        """Return where the answer came from for endpoint-level observability."""
        if isinstance(self.data, dict):
            source = self.data.get("source")
            if source in {"web_fallback", "web_fallback_attempted", "knowledge_memory", "web_cache"}:
                return source
        return "local"
    
    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "type": self.response_type.value,
            "error_code": self.error_code,
            "answer_source": self._resolve_answer_source(),
        }

@dataclass
class UserQuery:
    """User query model"""
    text: str
    category: Optional[str] = None
    user_id: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

@dataclass
class ExerciseInfo:
    """Exercise information model"""
    name: str
    muscles_targeted: List[str]
    difficulty: str
    sets_reps: str
    variations: List[str]
    how_to: str

@dataclass
class FoodInfo:
    """Food information model"""
    name: str
    category: str
    calories: float
    protein: float
    carbs: float
    fat: float
    fiber: float
    benefits: List[str]
    serving_size: str

@dataclass
class MealPlan:
    """Meal plan model"""
    goal: str
    duration: str
    meals: Dict[str, List[str]]
    daily_calories: int
    macros: Dict[str, float]

# Error codes
ERROR_CODES = {
    "INVALID_INPUT": "ERR_001",
    "INTENT_NOT_FOUND": "ERR_002",
    "KNOWLEDGE_BASE_ERROR": "ERR_003",
    "DATABASE_ERROR": "ERR_004",
    "INVALID_QUERY": "ERR_005",
    "INTERNAL_ERROR": "ERR_006"
}

# Success codes
SUCCESS_CODES = {
    "QUERY_PROCESSED": "SUC_001",
    "RECOMMENDATION_PROVIDED": "SUC_002",
    "INFO_RETRIEVED": "SUC_003"
}

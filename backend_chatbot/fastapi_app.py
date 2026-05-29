import logging
import os
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.chatbot_engine import FitnessChatbot
from app.models.response_model import ERROR_CODES


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Fitness Chatbot API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chatbot = FitnessChatbot()


class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Fitness Chatbot API",
    }


@app.post("/api/chat")
def chat(payload: ChatRequest):
    user_message = (payload.message or "").strip()
    if not user_message:
        raise HTTPException(
            status_code=400,
            detail={
                "success": False,
                "message": "Message cannot be empty",
                "type": "error",
                "error_code": ERROR_CODES["INVALID_INPUT"],
            },
        )

    logger.info("Processing message from user %s: %s", payload.user_id, user_message[:100])

    response = chatbot.process_query(user_message, payload.user_id)
    body = response.to_dict()

    if not response.success:
        raise HTTPException(status_code=400, detail=body)
    return body


@app.get("/api/greeting")
def greeting():
    try:
        greeting_msg = chatbot.get_greeting()
        return {
            "success": True,
            "message": greeting_msg,
            "type": "info",
        }
    except Exception as exc:
        logger.error("Error getting greeting: %s", str(exc))
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": "Error getting greeting",
                "type": "error",
            },
        )


@app.get("/api/knowledge/stats")
def knowledge_stats():
    try:
        stats = chatbot.knowledge_store.stats()
        return {
            "success": True,
            "message": "Knowledge stats retrieved",
            "data": stats,
            "type": "info",
        }
    except Exception as exc:
        logger.error("Error getting knowledge stats: %s", str(exc))
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": "Error retrieving knowledge stats",
                "type": "error",
                "error_code": ERROR_CODES["INTERNAL_ERROR"],
            },
        )


def _category_query(prefix: str, payload: ChatRequest):
    user_message = (payload.message or "").strip()
    if not user_message:
        raise HTTPException(
            status_code=400,
            detail={
                "success": False,
                "message": "Please provide a 'message' field",
                "type": "error",
                "error_code": ERROR_CODES["INVALID_INPUT"],
            },
        )

    response = chatbot.process_query(f"{prefix} {user_message}", payload.user_id)
    body = response.to_dict()
    if not response.success:
        raise HTTPException(status_code=400, detail=body)
    return body


@app.post("/api/fitness")
def fitness_query(payload: ChatRequest):
    return _category_query("fitness", payload)


@app.post("/api/health")
def health_query(payload: ChatRequest):
    return _category_query("health", payload)


@app.post("/api/diet")
def diet_query(payload: ChatRequest):
    return _category_query("diet", payload)


@app.post("/api/food")
def food_query(payload: ChatRequest):
    return _category_query("food", payload)


if __name__ == "__main__":
    # Default changed to 9000 to avoid conflict with other local backends
    port = int(os.environ.get("PORT", 9000))
    logger.info("Starting FastAPI Fitness Chatbot on port %s", port)

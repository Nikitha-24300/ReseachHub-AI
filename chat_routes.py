from fastapi import APIRouter
from pydantic import BaseModel
from .agent import ask_groq

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/")
def chat(request: ChatRequest):
    answer = ask_groq(request.question)
    return {"response": answer}
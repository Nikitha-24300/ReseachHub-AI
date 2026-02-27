from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

from database import Base, engine
from models.paper import Paper   # ✅ FIXED

Base.metadata.create_all(bind=engine)

from routers import papers
app.include_router(papers.router)

@app.get("/")
def root():
    return {"message": "ResearchHub AI Backend Running"}
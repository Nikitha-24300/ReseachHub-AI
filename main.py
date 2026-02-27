from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

from database import Base, engine
from models.paper import Paper
from models.workspace import Workspace
from models.user import User

Base.metadata.create_all(bind=engine)

# Include Routers
from routers import auth
from routers import papers
from routers import workspace

app.include_router(auth.router)
app.include_router(papers.router)
app.include_router(workspace.router)

@app.get("/")
def root():
    return {"message": "ResearchHub AI Backend Running"}

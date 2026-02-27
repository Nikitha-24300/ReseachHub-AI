from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from models.user import User
from models.workspace import Workspace
from models.paper import Paper
from auth.auth_routes import router as auth_router
from workspaces.workspace_routes import router as workspace_router
from workspaces.paper_routes import router as paper_router  # correct import

app = FastAPI(title="ResearchHub-AI")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router)
app.include_router(workspace_router)
app.include_router(paper_router)  # only include once

@app.get("/")
def root():
    return {"message": "ResearchHub-AI backend is running!"}
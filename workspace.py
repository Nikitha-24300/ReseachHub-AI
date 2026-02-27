from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.workspace import Workspace
from utils.auth import get_current_user

router = APIRouter(prefix="/workspaces", tags=["Workspaces"])

@router.post("/")
def create_workspace(
    name: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    workspace = Workspace(name=name, user_id=current_user.id)
    db.add(workspace)
    db.commit()
    db.refresh(workspace)
    return workspace


@router.get("/")
def get_workspaces(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return db.query(Workspace).filter(
        Workspace.user_id == current_user.id
    ).all()
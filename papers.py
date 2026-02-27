from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from models.paper import Paper
from models.workspace import Workspace
from utils.auth import get_current_user  # Fixed import

router = APIRouter(prefix="/papers", tags=["Papers"])

# Pydantic schemas
class PaperImport(BaseModel):
    title: str
    authors: str
    abstract: str
    workspace_id: int  # attach paper to workspace

class PaperOut(BaseModel):
    id: int
    title: str
    authors: str
    abstract: str
    workspace_id: int

    class Config:
       from_attributes = True

# Search papers (mock)
@router.get("/search", response_model=List[PaperOut])
def search_papers(query: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # For now, return last 5 papers added by this user
    papers = db.query(Paper).filter(Paper.user_id == current_user.id).order_by(Paper.id.desc()).limit(5).all()
    return papers

# Import a paper
@router.post("/import", response_model=PaperOut)
def import_paper(paper_data: PaperImport, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Check workspace exists and belongs to user
    workspace = db.query(Workspace).filter(Workspace.id == paper_data.workspace_id, Workspace.user_id == current_user.id).first()
    if not workspace:
        raise HTTPException(status_code=400, detail="Workspace not found or unauthorized")

    new_paper = Paper(
        title=paper_data.title,
        authors=paper_data.authors,
        abstract=paper_data.abstract,
        workspace_id=paper_data.workspace_id,
        user_id=current_user.id
    )
    db.add(new_paper)
    db.commit()
    db.refresh(new_paper)
    return new_paper
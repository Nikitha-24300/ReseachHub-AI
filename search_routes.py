from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.paper import Paper
from pydantic import BaseModel
from .embedding_utils import add_document

router = APIRouter()

class PaperCreate(BaseModel):
    title: str
    abstract: str
    workspace_id: int

@router.post("/import")
def import_paper(paper: PaperCreate, db: Session = Depends(get_db)):
    db_paper = Paper(
        title=paper.title,
        abstract=paper.abstract,
        workspace_id=paper.workspace_id
    )
    db.add(db_paper)
    db.commit()
    db.refresh(db_paper)

    add_document(paper.abstract)

    return {"message": "Paper stored and embedded"}
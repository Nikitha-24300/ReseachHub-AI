from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from models.paper import Paper
from auth import get_current_user

router = APIRouter(prefix="/papers", tags=["Papers"])


class PaperImport(BaseModel):
    title: str
    authors: str
    abstract: str
    source: str


@router.get("/search")
async def search_papers(query: str, current_user: User = Depends(get_current_user)):
    # Temporary mock results (we’ll replace with real academic API later)
    return {
        "papers": [
            {
                "title": f"Research about {query}",
                "authors": "John Doe",
                "abstract": "This paper discusses advanced concepts.",
                "source": "Mock Database"
            }
        ]
    }


@router.post("/import")
async def import_paper(
    paper_data: PaperImport,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_paper = Paper(
        title=paper_data.title,
        authors=paper_data.authors,
        abstract=paper_data.abstract,
        source=paper_data.source,
       
    )

    db.add(new_paper)
    db.commit()
    db.refresh(new_paper)

    return {
        "message": "Paper imported successfully",
        "paper": new_paper
    }
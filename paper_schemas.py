from pydantic import BaseModel

# Request model for creating a new paper
class PaperCreateModel(BaseModel):
    title: str
    content: str
    workspace_id: int

# Response model for returning paper info
class PaperResponseModel(BaseModel):
    id: int
    title: str
    content: str
    workspace_id: int

    class Config:
        from_attributes = True  # Use this instead of orm_mode in Pydantic v2
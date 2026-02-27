from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
from models.workspace import Workspace

class Paper(Base):
    __tablename__ = "papers"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"), nullable=False)

    # Relationships
    workspace = relationship("Workspace", back_populates="papers")
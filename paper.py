from sqlalchemy import Column, Integer, String
from database import Base

class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    authors = Column(String)
    abstract = Column(String)
    source = Column(String)




    print("Paper model loaded")
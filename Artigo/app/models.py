from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(Text)
    author = Column(String, index=True)
    category = Column(String, index=True)
    published_date = Column(DateTime)

import json

from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class News(Base):
    __tablename__ = "t_news"

    id = Column(String(255), primary_key=True)
    title = Column(String(512))
    author = Column(String(128))
    description = Column(String(2048))
    source = Column(String(255))
    source_link = Column(String(1024))
    image_url = Column(String(512))
    source_created_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP(), default=datetime.utcnow())


class NewsModel(BaseModel):
    title: str
    author: str
    description: str
    source: str
    source_link: str
    image_url: str
    source_created_at: str


def db_to_model(db_news_list: List[News]):
    model_news = [
        json.loads(
            NewsModel(
                title=db_news.title,
                author=db_news.author,
                description=db_news.description,
                source=db_news.source,
                source_link=db_news.source_link,
                image_url=db_news.image_url,
                source_created_at=db_news.source_created_at.strftime('%d-%m-%Y %H:%M:%S')
            ).model_dump_json()
        )

        for db_news in db_news_list
    ]
    return model_news

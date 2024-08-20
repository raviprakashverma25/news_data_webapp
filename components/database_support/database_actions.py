from datetime import datetime
from typing import List
from components.database_support import datasource_connection
from components.database_support.model import News, db_to_model
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_, func, Date


def get_db(app):
    return datasource_connection.db(app)


def save_news(db: SQLAlchemy, news_list):
    for news in news_list:
        db.session.merge(news)
        db.session.commit()


def get_news(db: SQLAlchemy):
    db_result_set = db.session.query(News).order_by(
        News.source_created_at.desc()
    ).limit(12).all()
    return db_to_model(db_result_set)


def get_news_bw_date(db: SQLAlchemy, s_date, e_date):
    db_result_set = db.session.query(News).filter(
        and_(
            News.source_created_at >= datetime.date(s_date),
            News.source_created_at <= datetime.date(e_date)
        )
    ).limit(12)
    return db_to_model(db_result_set)


def get_news_by_search(db: SQLAlchemy, query):
    db_result_set = db.session.query(News).filter(
        or_(
            func.lower(News.title).ilike(f"%{query.lower()}%"),
            func.lower(News.description).ilike(f"%{query.lower()}%")
        )
    ).limit(12)
    return db_to_model(db_result_set)


def get_analytics_author(db: SQLAlchemy):
    db_result_set = db.session.query(News.author,
                                     func.count(1).label("count")
                                     ).group_by(News.author).all()

    result_set = [
        {
            "value": db_row.author,
            "count": db_row.count,

        }
        for db_row in db_result_set
    ]
    return result_set


def get_analytics_sources(db: SQLAlchemy):
    db_result_set = db.session.query(News.source,
                                     func.count(1).label("count")
                                     ).group_by(News.source).all()

    result_set = [
        {
            "value": db_row.source,
            "count": db_row.count,

        }
        for db_row in db_result_set
    ]
    return result_set


def get_analytics_days(db: SQLAlchemy):
    db_result_set = db.session.query(func.cast(News.source_created_at, Date).label("source_date"),
                                     func.count(1).label("count")
                                     ).group_by(func.cast(News.source_created_at, Date)).all()

    result_set = [
        {
            "value": db_row.source_date,
            "count": db_row.count,

        }
        for db_row in db_result_set
    ]
    return result_set

#!/usr/bin/env python3
import json

from flask import Flask, request
from components.database_support import database_actions
from components.environment_support import constants
import logging

app = Flask(__name__)
db = database_actions.get_db(app)


@app.post('/show_news')
def show_news():
    request_data = request.get_json()
    news_list = []
    app.logger.info("News Data Requested from DB")
    if request_data:
        if request_data["query"]:
            news_list = database_actions.get_news_by_search(db=db,
                                                            query=request_data["query"])
        elif request_data["s_date"] and request_data["e_date"]:
            news_list = database_actions.get_news_bw_date(db=db,
                                                          s_date=request_data["s_date"],
                                                          e_date=request_data["e_date"])
        else:
            news_list = database_actions.get_news(db)
    else:
        news_list = database_actions.get_news(db)
    return news_list, 200


@app.post("/news_sources_count")
def news_sources_count():
    app.logger.info("Analytics on News sources count")
    news_sources = database_actions.get_analytics_sources(db)

    return news_sources, 200


@app.post("/news_authors_count")
def news_authors_count():
    app.logger.info("Analytics on News Authors count")
    news_authors = database_actions.get_analytics_author(db)

    return news_authors, 200


@app.post("/news_stat_days")
def news_stat_days():
    app.logger.info("Analytics on News Day Stats")
    news_stat = database_actions.get_analytics_days(db)

    return news_stat, 200


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


if __name__ == "__main__":

    app.run(debug=True, host=constants.DATA_ANALYZER_HOST, port=constants.DATA_ANALYZER_PORT)

#!/usr/bin/env python3

from flask import Flask
from applications.data_collector import process
from components.rest_support import external_news_api
from components.database_support import database_actions
from components.environment_support import constants
import logging

app = Flask(__name__)
db = database_actions.get_db(app)


@app.post("/collect_latest_news")
def collect_latest_news():
    app.logger.info("DATA COLLECTION REQUESTED")
    news_json_data = external_news_api.get_recent_news()
    if not (news_json_data["data"] and len(news_json_data["data"]["news_list"]) > 0):
        app.logger.error("NO NEWS FOUND")
        return 'No news found', 404

    model_data = process.parse_data_from_api(news_json_data["data"]["news_list"])
    database_actions.save_news(db, model_data)
    app.logger.info("DATA COLLECTION SUCCESS")
    return "DATA COLLECTION SUCCESS", 200


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


if __name__ == "__main__":

    app.run(debug=True, host=constants.DATA_COLLECTOR_HOST, port=constants.DATA_COLLECTOR_PORT)

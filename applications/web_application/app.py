#!/usr/bin/env python3

from flask import Flask, render_template, request
import os
from components.environment_support import constants
from applications.web_application import api_caller
import logging
from prometheus_client import Counter, generate_latest


app = Flask(__name__)


requests_counter = Counter("app_requests_total", "Total app HTTP requests.")


@app.get("/")
def main():
    requests_counter.inc()
    news_list = api_caller.fetch_news(None)
    return render_template("home.html", news_list=news_list)


@app.post("/search")
def search():
    requests_counter.inc()
    news_list = api_caller.fetch_news(request.form)
    return render_template("home.html", news_list=news_list)


@app.get("/health")
def health():
    return render_template("health.html")


@app.get("/metrics")
def metrics():
    return render_template("metrics.html", metrics=generate_latest())


@app.get("/analytics")
def analytics():
    requests_counter.inc()
    analytics_result = api_caller.fetch_analytics()
    return render_template("analytics.html", analytics_result=analytics_result)  # generate_latest()


@app.post("/updateNews")
def update_news():
    return '''

    '''


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    app.run(debug=True, host=constants.WEB_APPLICATION_HOST, port=constants.WEB_APPLICATION_PORT)

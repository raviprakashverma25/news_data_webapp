import requests
from components.environment_support.constants import DATA_COLLECTOR_ENDPOINT
from components.environment_support.constants import DATA_ANALYZER_ENDPOINT
from components.environment_support.constants import request_header


def fetch_news(request_data):
    response = []
    if request_data is None:
        response = requests.post(
            DATA_ANALYZER_ENDPOINT + "/show_news",
            json={},
            headers=request_header
        )
        print(response)
    else:
        if request_data.get("query"):
            response = requests.post(
                DATA_ANALYZER_ENDPOINT + "/show_news",
                json={"query": request_data.get("query")},
                headers=request_header
            )
        elif request_data.get("s_date") and request_data.get("e_date"):
            response = requests.post(
                DATA_ANALYZER_ENDPOINT + "/show_news",
                json={
                    "s_date": request_data.get("s_date"),
                    "e_date": request_data.get("e_date"),
                },
                headers=request_header
            )
    return response.json()


def fetch_analytics():
    news_sources_count = requests.post(
        DATA_ANALYZER_ENDPOINT + "/news_sources_count"
    )
    news_authors_count = requests.post(
        DATA_ANALYZER_ENDPOINT + "/news_authors_count"
    )
    news_stats_days = requests.post(
        DATA_ANALYZER_ENDPOINT + "/news_stat_days"
    )
    analytics = {
        "sources": news_sources_count.json(),
        "authors": news_authors_count.json(),
        "day_stat": news_stats_days.json()
    }

    return analytics


def refresh_data_from_api():
    response = requests.get(
        DATA_COLLECTOR_ENDPOINT + "/collect_latest_news"
    )
    return response

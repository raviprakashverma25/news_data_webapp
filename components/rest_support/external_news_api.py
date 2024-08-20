import requests


def get_recent_news():
    response = requests.get('https://inshorts.com/api/en/news?category=all_news&max_limit=1000&include_card_data=true')

    return response.json()

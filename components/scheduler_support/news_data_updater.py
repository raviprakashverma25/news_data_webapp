import requests
from components.environment_support.constants import DATA_COLLECTOR_ENDPOINT
import sys

response = requests.get(
    DATA_COLLECTOR_ENDPOINT + "/collect_latest_news"
)
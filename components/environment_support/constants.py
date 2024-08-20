import os

ENVIRONMENT = os.getenv("ENVIRONMENT") if os.getenv("ENVIRONMENT") else "DEV"

WEB_APPLICATION_HOST = os.getenv("WEB_APPLICATION_HOST") if os.getenv("WEB_APPLICATION_HOST") else "0.0.0.0"
DATA_COLLECTOR_HOST = os.getenv("DATA_COLLECTOR_HOST") if os.getenv("DATA_COLLECTOR_HOST") else "0.0.0.0"
DATA_ANALYZER_HOST = os.getenv("DATA_ANALYZER_HOST") if os.getenv("DATA_ANALYZER_HOST") else "0.0.0.0"

WEB_APPLICATION_PORT = os.getenv("WEB_APPLICATION_PORT") if os.getenv("WEB_APPLICATION_PORT") else "8080"
DATA_COLLECTOR_PORT = os.getenv("DATA_COLLECTOR_PORT") if os.getenv("DATA_COLLECTOR_PORT") else "9081"
DATA_ANALYZER_PORT = os.getenv("DATA_ANALYZER_PORT") if os.getenv("DATA_ANALYZER_PORT") else "9091"


DATA_ANALYZER_ENDPOINT = ("https://" if ENVIRONMENT == "PROD" else "http://") + DATA_ANALYZER_HOST + ":" + DATA_ANALYZER_PORT
WEB_APPLICATION_ENDPOINT = ("https://" if ENVIRONMENT == "PROD" else "http://") + WEB_APPLICATION_HOST + ":" + WEB_APPLICATION_PORT
DATA_COLLECTOR_ENDPOINT = ("https://" if ENVIRONMENT == "PROD" else "http://") + DATA_COLLECTOR_HOST + ":" + DATA_COLLECTOR_PORT

DATABASE_URL = os.getenv("DATABASE_URL")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

request_header={"Content-Type": "application/json"}

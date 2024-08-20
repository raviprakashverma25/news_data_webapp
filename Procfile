web: gunicorn applications.web_application.app:app
data_collector: gunicorn applications.data_collector.app:app --bind 0.0.0.0:9091
data_analyzer: gunicorn applications.data_analyzer.app:app --bind 0.0.0.0:9081
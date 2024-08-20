web: gunicorn applications.web_application.app:app --bind 0.0.0.0:8080
datacollector: gunicorn applications.data_collector.app:app --bind 0.0.0.0:9081
dataanalyzer: gunicorn applications.data_analyzer.app:app --bind 0.0.0.0:9091

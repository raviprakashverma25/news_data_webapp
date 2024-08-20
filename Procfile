web: gunicorn applications.web_application.app:app
datacollector: gunicorn applications.data_collector.app:app --bind 0.0.0.0:9091
dataanalyzer: gunicorn applications.data_analyzer.app:app --bind 0.0.0.0:9081
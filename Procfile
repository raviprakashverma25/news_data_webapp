web: gunicorn applications.web_application.app:app --bind 0.0.0.0:8080
data_collector: gunicorn applications.data_collector.app:app --bind 0.0.0.0:9091
data_analysis: gunicorn applications.data_analysis.app:app --bind 0.0.0.0:9081
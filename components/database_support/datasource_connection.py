from components.environment_support.constants import ENVIRONMENT
from components.environment_support.constants import DATABASE_URL, DB_HOST, DB_PORT
from components.environment_support.constants import DB_NAME, DB_USERNAME, DB_PASSWORD
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

URI = DATABASE_URL if ENVIRONMENT == "PROD" else (
        "postgresql://"
        + DB_USERNAME + ":"
        + DB_PASSWORD + "@"
        + DB_HOST + ":"
        + DB_PORT + "/"
        + DB_NAME
)

SQLALCHEMY_DATABASE_URI = str.replace(URI, "postgres://", "postgresql://")


def db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    return SQLAlchemy(app)


def get_session():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    return db_session

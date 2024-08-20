from components.database_support import datasource_connection
from components.database_support.model import Base

db_session = datasource_connection.get_session()
Base.metadata.create_all(db_session.bind.engine)
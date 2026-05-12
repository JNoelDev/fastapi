from collections.abc import Generator
from sqlalchemy.orm import Session
from .database_config import DatabaseConfig
from .database_engine import DatabaseEngine
from .database_session import DatabaseSession


_config = DatabaseConfig()
_engine = DatabaseEngine(config=_config)
_session = DatabaseSession(engine=_engine.engine, config=_config)

def get_db() -> Generator[Session,None,None]:
    db = _session.create_session()
    try:
        yield db
    finally:
        db.close()

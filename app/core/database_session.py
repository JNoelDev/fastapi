from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker,Session
from .database_config import DatabaseConfig 

class DatabaseSession:

    def __init__(self,engine:Engine,config:DatabaseConfig) ->None:
        self.config=config
        self._session_factory=self._create_session_factory(engine)

    def _create_session_factory(self,engine:Engine) ->sessionmaker:
        return sessionmaker(
            bind=engine,
            autoflush=self.config.AUTOFLUSH,
            autocommit=self.config.AUTOCOMMIT,
            class_=Session
            )
    
    def create_session(self) ->Session:
        return self._session_factory()
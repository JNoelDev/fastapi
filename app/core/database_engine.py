from sqlalchemy import create_engine,Engine
from sqlalchemy.pool import QueuePool
from .database_config import DatabaseConfig

class DatabaseEngine:

    def __init__(self,config:DatabaseConfig)->None:
        self.config=config
        self._engine=self._create_engine

    def _create_engine(self) -> Engine:
        return create_engine(
            self.config.DATABASE_URL,
            poolclass=QueuePool,
            pool_pre_ping=self.config.POOL_PRE_PING,
            pool_size=self.config.POOL_SIZE,
            max_overflow=self.config.MAX_OVERFLOW,
            pool_timeout=self.config.POOL_TIMEOUT
        )
    
    @property
    def engine(self) ->Engine:
        return self._engine 

        
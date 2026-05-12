from .config import Settings


class DatabaseConfig:

    DATABASE_URL : str = Settings.database_url 
    POOL_PRE_PING : bool = getattr(Settings,"db_pool_pre_ping",True)
    POOL_SIZE : int = getattr(Settings,"db_pool_size",5)
    MAX_OVERFLOW : int = getattr(Settings,"db_max_overflow",10)
    POOL_TIMEOUT : int = getattr(Settings,"db_pool_timeout",30)

    AUTOFLUSH : bool = getattr(Settings,"db_autoflush",False)
    AUTOCOMMIT : bool = getattr(Settings,"db_autocommit",False)
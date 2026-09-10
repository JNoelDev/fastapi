from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from app.modules.users.register.model import User
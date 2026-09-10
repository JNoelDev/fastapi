from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.models.base import UUIDStampz
from app.db.base import Base


class User(Base,UUIDStampz):

    __tablename__="users"

    first_name:Mapped[str]=mapped_column(String(20),nullable=False,index=True)

    last_name:Mapped[str]=mapped_column(String(20),nullable=False,index=True)

    email:Mapped[str]=mapped_column(String(60),nullable=False,index=True,unique=True)

    password:Mapped[str]=mapped_column(String(150),nullable=False)
from sqlalchemy import (
    Integer,String,DateTime,Boolean,func,Date,ForeignKey
    )
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(
        Integer,primary_key=True,nullable=False,autoincrement=True,index=True
        )
    
    username : Mapped[str] = mapped_column(String(255),nullable=False)
    email : Mapped[str] = mapped_column(String(255),unique=True,nullable=False)
    password_hash : Mapped[str] = mapped_column(String(255),nullable=False)

    email_verified : Mapped[bool] = mapped_column(Boolean,nullable=False)
    email_token : Mapped[str|None] = mapped_column(String(255),nullable=False,unique=True)
    email_token_expires : Mapped[datetime|None] = mapped_column(DateTime(timezone=True))

    phone : Mapped[str|None] = mapped_column(String(255))
    sexe : Mapped[str] = mapped_column(String(150),nullable=False)
    cin : Mapped[str|None] = mapped_column(String(255))
    verified : Mapped[bool] = mapped_column(Boolean,default=False,nullable=False)
    code_user : Mapped[str] = mapped_column(String(255),nullable=False,unique=True,index=True)

    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
        )
    
    profile : Mapped["Profile"] = relationship(
        "Profile",back_populates="user",uselist=False,cascade="all,delete-orphan")
    

class Profile(Base):

    __tablename__ = "profiles"

    id : Mapped[int] = mapped_column(
        Integer,primary_key=True,nullable=False,autoincrement=True
        )
    user_id : Mapped[int] = mapped_column(Integer,ForeignKey("users.id"),nullable=False)
    
    full_name : Mapped[str|None] = mapped_column(String(255))
    profile_picture : Mapped[str|None] = mapped_column(String(255))
    relationship_status : Mapped[str|None] = mapped_column(String(200))
    birth_date : Mapped[Date|None] = mapped_column(Date)
    badge_blue : Mapped[bool] = mapped_column(Boolean,default=False,nullable=False)

    user : Mapped["User"] = relationship("User",back_populates="profile")

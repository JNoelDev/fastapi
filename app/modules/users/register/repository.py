from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select
from app.modules.users.register.model import User

class UserRepository:
    def __init__(self,db:AsyncSession):
        self.db=db

    async def get_by_email(self,email:str) -> User|None:
        user = await self.db.execute(Select(User).where(User.email==email))
        return user.scalar_one_or_none()

    async def create(self,data:dict) ->User:
        user=User(**data)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

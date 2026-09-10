from fastapi import status,HTTPException
from app.core.security import hash_password
from app.modules.users.register.model import User
from app.modules.users.register.repository import UserRepository
from app.modules.users.register.schema import Register

class UserService:
    def __init__(self,repo:UserRepository) ->None:
        self.repo=repo

    async def register_1(self,payload:Register) -> User:
        existing_email = await self.repo.get_by_email(payload.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,detail="User already register"
            )

        user_data = {
            "first_name":payload.first_name,
            "last_name":payload.last_name,
            "email":payload.email,
            "password":hash_password(payload.password)
        }

        return await self.repo.create(user_data)



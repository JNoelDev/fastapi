from app.modules.users.register.repository import UserRepository
from app.modules.users.register.schema import Register

class UserService:
    def __init__(self,repo:UserRepository):
        self.repo=repo

    async def register_1(payload:Register):
        pass
from fastapi import APIRouter,status
from app.modules.users.register.schema import Register,ResponseRegister
from app.modules.users.register.service import UserService
from app.modules.users.register.repository import UserRepository

router = APIRouter(prefix="/users", tags=["/users"])


def _get_service() -> UserService:
    user_service=UserService()

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Create a account",
    response_model=ResponseRegister  
)
async def register(payload:Register):
    pass
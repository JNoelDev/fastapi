from fastapi import APIRouter,status,Depends
from app.modules.users.register.schema import Register,ResponseRegister
from app.modules.users.register.service import UserService
from app.modules.users.register.repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter(prefix="/users", tags=["/users"])


def _get_service(db:AsyncSession=Depends(get_db)) -> UserService:
    user_repo=UserRepository(db)
    return UserService(user_repo)

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Create a account",
    response_model=ResponseRegister  
)
async def register(payload:Register,service:UserService=Depends(_get_service)):
    user = await service.register_1(payload)
    return ResponseRegister.model_validate(user)
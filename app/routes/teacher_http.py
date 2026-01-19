from typing import List, Set

from fastapi import APIRouter, Depends, Security

from app.database.models import User
from app.enums import Permission
from app.schemas import TeacherOdoo
from app.services import UserService

from .dependencies import get_current_user, get_user_service

teacher_router: APIRouter = APIRouter(prefix="/profesores", tags=["Odoo Teachers"])


@teacher_router.get(path="/", response_model=List[TeacherOdoo])
async def route_get_teachers(
    user_service: UserService = Depends(get_user_service),
    current_user: User = Security(
        dependency=get_current_user, scopes=[Permission.READ_EXTERNAL_USERS]
    ),
) -> List[TeacherOdoo]:
    users_ids: Set[int] = {
        user.external_reference
        for user in await user_service.get_users(is_active=True)
        if user.external_reference
    }

    return user_service.get_external_users(teacher_ids=users_ids)

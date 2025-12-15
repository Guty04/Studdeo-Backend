from .contract import Contract, ContractCreate
from .email import UserBaseEmail
from .odoo import (
    CourseOdoo,
    CourseWithSales,
    DetailSaleOdoo,
    LessonOdoo,
    SaleOdoo,
    StudentOdoo,
    TeacherOdoo,
)
from .role import RoleDB
from .token import Token
from .user import User, UserContract, UserCreate, UserDB

__all__: list[str] = [
    "Contract",
    "ContractCreate",
    "CourseOdoo",
    "CourseWithSales",
    "DetailSaleOdoo",
    "LessonOdoo",
    "RoleDB",
    "SaleOdoo",
    "StudentOdoo",
    "TeacherOdoo",
    "Token",
    "User",
    "UserDB",
    "UserCreate",
    "UserBaseEmail",
    "UserContract",
]

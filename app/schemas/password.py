from pydantic import BaseModel, Field


class ChangePassword(BaseModel):
    password: str = Field(min_length=8, pattern=r".*[A-Z].*")
    repeat_password: str = Field(min_length=8, pattern=r".*[A-Z].*")

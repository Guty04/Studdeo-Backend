from pydantic import BaseModel, HttpUrl


class UserCreateEmail(BaseModel):
    name: str
    lastname: str
    frontend_url: HttpUrl
    year: int

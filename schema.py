from typing import Optional
import pydantic
from models import Session, get_user


class CreateUser(pydantic.BaseModel):
    email: str
    password: str

    @pydantic.validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('password is too short')
        return value


class PatchUser(pydantic.BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]

    @pydantic.validator('password')
    def valdate_password(cls, value):
        if len(value) < 8:
            raise ValueError('password is too short')
        return value


class CreateAdv(pydantic.BaseModel):
    title: str
    description: str
    user_id: int

    @pydantic.validator('user_id')
    def check_existence_user(cls, id):
        with Session() as session: get_user(id, session)
        return id


class PatchAdv(pydantic.BaseModel):
    title: Optional[str]
    description: Optional[str]
    user_id: Optional[str]

from typing import Type, Union

import pydantic

from exceptions import ApiException
from schema import CreateUser, CreateAdv

SCHEMA_TYPE = Union[Type[CreateUser], Type[CreateAdv]]


def validate(input_data: dict, validation_model):
    try:
        model_item = validation_model(**input_data)
    except pydantic.ValidationError as er:
        raise ApiException(400, er.errors())
    return model_item.dict(exclude_none=True)

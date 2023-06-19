from pydantic import BaseModel, Field


class LoginDto(BaseModel):
    phone_no: str = Field(alias='phoneNo')


class TokenDto(BaseModel):
    token_type: str
    expires_in: int
    access_token: str


class UserDto(BaseModel):
    phone_no: str = Field(alias='phoneNo')

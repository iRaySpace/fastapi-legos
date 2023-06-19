import time
import jwt
from typing import Dict
from auth.app.config import get_settings
from auth.domain.dto import LoginDto, TokenDto, UserDto


def _sign_jwt(sub: str, expires_in=300) -> TokenDto:
    epoch = int(time.time())
    payload = {
        'sub': sub,
        'iat': epoch,
        'exp': epoch + expires_in,
    }
    return {
        'token_type': 'Bearer',
        'expires_in': expires_in,
        'access_token': jwt.encode(
            payload,
            get_settings().secret_key,
            get_settings().algorithm,
        ),
    }


def _decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token,
            get_settings().secret_key,
            get_settings().algorithm,
        )
        return decoded_token if decoded_token['exp'] >= int(time.time()) else None
    except Exception as e:
        return None


def login(data: LoginDto):
    return _sign_jwt(data.phone_no)


def verify_token(token: str) -> UserDto:
    data = _decode_jwt(token)
    return UserDto(phoneNo=data.get('sub')) if data else None

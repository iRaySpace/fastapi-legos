from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.security import HTTPBearer
from auth.domain.dto import LoginDto, TokenDto, UserDto
from auth.domain import usecase
from auth.data import auth_repository

api_router = APIRouter()
http_bearer = HTTPBearer()


async def _token_auth(bearer: HTTPBearer = Depends(http_bearer)) -> UserDto:
    data = usecase.process_token(bearer.credentials, auth_repository)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return data


@api_router.get('/ping')
async def send_pong(user_data: UserDto = Depends(_token_auth)):
    return {'message': f'Hello, {user_data.phone_no}!'}


@api_router.post('/login')
async def process_login(login_data: LoginDto) -> TokenDto:
    return usecase.login(login_data, auth_repository)

from fastapi import Depends
from fastapi.routing import APIRouter
from role.app.auth import RoleBasedAuthorization

api_router = APIRouter()


@api_router.get('/ping')
async def send_pong():
    return {'message': 'pong'}


@api_router.get('/user_ping', dependencies=[Depends(RoleBasedAuthorization('user'))])
async def send_user_pong():
    return {'message': 'user pong'}


@api_router.get('/superuser_ping', dependencies=[Depends(RoleBasedAuthorization('superuser'))])
async def send_superuser_pong():
    return {'message': 'superuser pong'}

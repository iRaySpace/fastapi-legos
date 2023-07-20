import redis
from fastapi.routing import APIRouter
from caching.domain import usecase

api_router = APIRouter()


@api_router.get('/ping')
async def send_pong():
    return {'message': 'pong'}


@api_router.get('/test_data')
async def send_data():
    return usecase.get_test_data()

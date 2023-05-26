from fastapi.routing import APIRouter

api_router = APIRouter()


@api_router.get('/ping')
async def send_pong():
    return {'message': 'pong'}

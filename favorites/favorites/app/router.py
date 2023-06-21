from fastapi.routing import APIRouter
from favorites.domain import usecase
from favorites.domain.dto import FavoriteCreateDto
from favorites.data import video_repository, favorite_repository

api_router = APIRouter()


@api_router.get('/ping')
async def send_pong():
    return {'message': 'pong'}


@api_router.get('/videos')
async def send_videos():
    return usecase.get_videos(video_repository)


@api_router.get('/favorites')
async def send_favorites():
    return usecase.get_favorites(favorite_repository)


@api_router.post('/favorites')
async def process_favorites(favorite: FavoriteCreateDto):
    return usecase.set_as_favorite(favorite_repository, video_repository, favorite)

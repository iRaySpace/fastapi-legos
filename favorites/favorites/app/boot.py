from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from favorites.app.router import api_router
from favorites.domain.error import VideoNotFoundError, AlreadyInFavoritesError


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=api_router, prefix='/api')
    app.add_exception_handler(VideoNotFoundError, video_not_found_handler)
    app.add_exception_handler(AlreadyInFavoritesError, already_in_favorites_handler)
    return app


async def video_not_found_handler(request: Request, err: VideoNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, 
        content={"message": f"{err.id} cannot be found." },
    )


async def already_in_favorites_handler(request: Request, err: AlreadyInFavoritesError):
    return JSONResponse(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED, 
        content={"message": f"{err.id} is already in favorites." },
    )

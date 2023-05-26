from fastapi import FastAPI
from template.app.router import api_router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=api_router, prefix='/api')
    return app

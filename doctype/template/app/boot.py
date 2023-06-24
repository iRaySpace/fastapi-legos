from fastapi import FastAPI
from template.app.router import get_router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=get_router(), prefix='/doctypes')
    return app

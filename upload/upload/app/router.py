import os
import shutil
from fastapi import UploadFile
from fastapi.routing import APIRouter

api_router = APIRouter()

@api_router.get('/ping')
async def send_pong():
    return {'message': 'pong'}


@api_router.post('/upload')
async def create_upload_file(file: UploadFile):
    upload_dir = os.path.join(os.getcwd(), "public")
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    with open(os.path.join(upload_dir, file.filename), 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {'filename': file.filename}

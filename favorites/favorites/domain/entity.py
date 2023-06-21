from pydantic import BaseModel


class Video(BaseModel):
    id: str
    title: str
    description: str


class Favorite(BaseModel):
    id: str
    video_id: str

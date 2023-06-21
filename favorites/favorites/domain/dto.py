from pydantic import BaseModel


class FavoriteCreateDto(BaseModel):
    video_id: str

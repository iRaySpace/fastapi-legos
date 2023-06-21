import uuid
from typing import List, Optional
from favorites.domain.dto import FavoriteCreateDto
from favorites.domain.entity import Favorite

data = []


def create(favorite: FavoriteCreateDto) -> Favorite:
    favorite = Favorite(**{
        **favorite.dict(),
        'id': str(uuid.uuid4()),
    })
    data.append(favorite)
    return favorite


def get_all() -> List[Favorite]:
    return data


def get(favorite_id: str) -> Optional[Favorite]:
    result = [x for x in data if x.video_id == favorite_id]
    return result[0] if data else None

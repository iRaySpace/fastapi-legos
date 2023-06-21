import uuid
from typing import List, Optional
from favorites.domain.entity import Video


data = [
        Video(
            id=str(uuid.uuid4()),
            title='Learn HTML',
            description='Hypertext Markup Language',
        ),
        Video(
            id=str(uuid.uuid4()),
            title='Learn Rust',
            description='World\'s most favorite programming language',
        ),
    ]


def get_all() -> List[Video]:
    return data


def get(video_id: str) -> Optional[Video]:
    video = [x for x in data if x.id == video_id]
    return video[0] if video else None

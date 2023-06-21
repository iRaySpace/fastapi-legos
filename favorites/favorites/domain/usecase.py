from favorites.domain.entity import Video, Favorite
from favorites.domain.dto import FavoriteCreateDto
from favorites.domain.error import VideoNotFoundError, AlreadyInFavoritesError


def get_videos(repository):
    return repository.get_all()


def set_as_favorite(repository, video_repository, favorite: FavoriteCreateDto):
    video = video_repository.get(favorite.video_id)

    if not video:
        raise VideoNotFoundError(favorite.video_id)
    existing_favorite = repository.get(favorite.video_id)

    if existing_favorite:
        raise AlreadyInFavoritesError(favorite.video_id)

    return repository.create(favorite)


def get_favorites(repository):
    return repository.get_all()


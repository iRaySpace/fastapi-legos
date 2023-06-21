class VideoNotFoundError(Exception):
    def __init__(self, id: str):
        self.id = id


class AlreadyInFavoritesError(Exception):
    def __init__(self, id: str):
        self.id = id

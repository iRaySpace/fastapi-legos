from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer

http_bearer = HTTPBearer()


class RoleBasedAuthorization:
    def __init__(self, role: str):
        self.role = role

    async def __call__(self, bearer: HTTPBearer = Depends(http_bearer)):
        if self.role != bearer.credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate credentials',
                headers={'WWW-Authenticate': 'Bearer'},
            )

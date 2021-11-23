from typing import Optional

from fastapi import APIRouter, HTTPException, status

from backend import utils

router = APIRouter()


@router.get("/users")
def get(
        id: Optional[str] = None,
        name: Optional[str] = None,
        email: Optional[str] = None):
    if utils.optionals_to_int(id, name, email) != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You need to provide exactly 1 query parameters!"
        )
    elif id:
        return {"id": id}
    elif name:
        return {"name": name}
    elif email:
        return {"email": email}

"""Template App
"""
from fastapi import APIRouter, Depends

from api.dependencies import get_firebase_user


simple_router = APIRouter()


@simple_router.get('/firebase_user')
async def firebase_user(
    user = Depends(get_firebase_user)
):
    """Test endpoint that depends on authenticated firebase
    """
    return user

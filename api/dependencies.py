"""Template App
"""
import logging

from fastapi import HTTPException
from starlette.requests import Request

from firebase_admin import auth


def get_firebase_user(request: Request):
    """Get the user details from Firebase, based on TokenID in the request

    :param request: The HTTP request
    """
    id_token = request.headers.get('Authorization')
    if not id_token:
        raise HTTPException(status_code=400, detail='TokenID must be provided')

    try:
        claims = auth.verify_id_token(id_token)
        return claims
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=401, detail='Unauthorized')

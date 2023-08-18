import asyncio

from fastapi import APIRouter, HTTPException


# from dependencies import get_instagram_photos

router = APIRouter(prefix='', tags=['Instagram'])


@router.get("/getPhotos")
async def get_photos(username: str, max_count: int):
    return {"urls": [username, max_count]}



import asyncio

from fastapi import APIRouter, HTTPException

from dependencies import get_instagram_photo_links

router = APIRouter(prefix='', tags=['Instagram'])


@router.get("/getPhotos")
async def get_photos(username: str, max_count: int):
    result = await get_instagram_photo_links()
    return {"urls": result}



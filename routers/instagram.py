from fastapi import APIRouter

router = APIRouter(prefix='', tags=['Instagram'])


@router.get("/getPhotos")
async def get_photos(username: str, max_count: int):
    return {
        "urls": [username, max_count]
    }

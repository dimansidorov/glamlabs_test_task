from fastapi import APIRouter
from fastapi.responses import JSONResponse
from dependencies import get_instagram_photo_links, EmptyPageException

router = APIRouter(prefix='', tags=['Instagram'])


@router.get("/getPhotos")
async def get_photos(username: str, max_count: int):
    try:
        result = await get_instagram_photo_links(username, max_count)
    except EmptyPageException:
        return JSONResponse(
            content={'error': 'This profile is empty or does not exist'},
            status_code=400
        )
    else:
        return JSONResponse(
            content={"urls": result},
            status_code=200
        )



from fastapi import APIRouter
from fastapi.responses import JSONResponse
from dependencies import get_instagram_photo_links, EmptyPageException, PageLoadError

router = APIRouter(prefix='', tags=['Instagram'])


@router.get("/getPhotos")
async def get_photos(username: str, max_count: int):
    try:
        result = await get_instagram_photo_links(username, max_count)
    except EmptyPageException:
        return JSONResponse(
            content={'message': 'This profile is empty or does not exist'},
            status_code=400
        )
    except PageLoadError:
        return JSONResponse(
            content={'error': 'Origin Is Unreachable. Please try again later.'},
            status_code=523
        )
    else:
        return JSONResponse(
            content={"urls": result},
            status_code=200
        )



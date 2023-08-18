from fastapi import FastAPI
from routers.instagram import router as instagram_router

app = FastAPI(title="Glamlabs Test App")

app.include_router(instagram_router)

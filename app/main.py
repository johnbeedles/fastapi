from fastapi import FastAPI
from app.routers import auth
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# this will create the tables in the database, not longer needed now using alembic
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# get root, not really used currently
@app.get("/")
async def root():
    return {
        "message": "Welcome to my API - by John Beedles",
        "docs": "view documentation here: http://127.0.0.1:8000/docs",
        "redoc": "view documentation here: http://127.0.0.1:8000/redoc"
    }


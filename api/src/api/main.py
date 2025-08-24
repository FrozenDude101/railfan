from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import create_engine, StaticPool

from api.routes import UserRouter
from api.db import UserController

engine = create_engine(
    "sqlite://",
    connect_args={'check_same_thread':False},
    poolclass=StaticPool
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:3000",
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(UserRouter(UserController(engine)).router)


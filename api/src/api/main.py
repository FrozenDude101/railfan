from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import create_engine, StaticPool, SQLModel

from api.testData import loadTestData

import os
os.remove("test.db")

engine = create_engine(
    url = "sqlite:///test.db",
    connect_args = { 'check_same_thread': False },
    poolclass = StaticPool,
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

SQLModel.metadata.create_all(engine)

loadTestData(engine)

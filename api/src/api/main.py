from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import create_engine, StaticPool, SQLModel
import os

from api.testData import loadTestData

def main() -> None:
    os.remove("test.db")
    engine = create_engine(
        url = "sqlite:///test.db",
        connect_args = { 'check_same_thread': False },
        poolclass = StaticPool
    )

    SQLModel.metadata.create_all(engine)
    loadTestData(engine)

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

if __name__ == "__main__":
    main()

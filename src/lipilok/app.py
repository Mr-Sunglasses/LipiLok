from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from spello.model import SpellCorrectionModel
import logging
import os
from logging.config import dictConfig

from .config import get_settings
from .logging import LogConfig
from .api import router
from .routers.endpoints import sp
from .models import Base
from .database import engine


dictConfig(LogConfig())
logger = logging.getLogger("lipilok")

origins = ["*"]

current_file_directory = os.path.dirname(os.path.abspath(__file__))

SELECTED_MODEL = get_settings().MODEL or "en_large"

SELECTED_MODEL = (
    SELECTED_MODEL
    if SELECTED_MODEL in ["en", "en_large", "hi", "hi_large"]
    else "en_large"
)


MODEL_PATH = os.path.abspath(
    os.path.join(
        current_file_directory, "..", "..", f"language_models/{SELECTED_MODEL}.pkl"
    )
)

MODEL_SAVE_DIR = os.path.abspath(
    os.path.join(current_file_directory, "..", "..", "language_models")
)


def configure_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    sp.load(model_path=MODEL_PATH)
    yield
    sp.save(model_save_dir=MODEL_SAVE_DIR)


def create_app() -> FastAPI:
    app = FastAPI(title="lipilok", lifespan=lifespan)
    configure_cors(app=app)
    Base.metadata.create_all(bind=engine)
    app.include_router(router=router)

    return app


logger.info("Starting Lipilok")
app = create_app()

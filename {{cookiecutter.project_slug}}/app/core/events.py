from typing import Callable

from fastapi import FastAPI
from loguru import logger


def preload_model():
    """
    In order to load model on memory to each worker
    """
    from app.services.predict import MachineLearningModelHandlerScore

    MachineLearningModelHandlerScore.get_model()


def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        preload_model()

    return start_app
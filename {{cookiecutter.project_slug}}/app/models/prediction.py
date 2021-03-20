from pydantic import BaseModel
from typing import Optional


class ServiceResponse(BaseModel):
    prediction: float


class HealthResponse(BaseModel):
    status: bool

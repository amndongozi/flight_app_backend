from typing import Optional, Dict
from pydantic import BaseModel


class FlightRequest(BaseModel):
    UNIQUE_CARRIER: str
    ORIGIN: str
    DEST: str
    DEP_TIME_CATEGORY: str
    DAY_OF_WEEK: int
    MONTH: int
    DAY_OF_MONTH: int
    DISTANCE: float
    ROUTE_DELAY_RATE: float


class PredictionResponse(BaseModel):
    delay_probability: float
    delay_risk: str


class ChatRequest(BaseModel):
    query: str
    context: Optional[Dict] = None

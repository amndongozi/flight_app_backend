from fastapi import FastAPI
from schemas import FlightRequest, PredictionResponse
from predictor import predict_delay
from agent import generate_agent_response
from typing import Optional
from schemas import ChatRequest
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(title="Flight Delay Intelligence API")

@app.post("/predict", response_model=PredictionResponse)
def predict(request: FlightRequest):
    prob, risk = predict_delay(request.dict())
    return {
        "delay_probability": prob,
        "delay_risk": risk
    }


@app.post("/chat")
def chat(request: ChatRequest):
    response = generate_agent_response(
        request.query,
        request.context or {}
    )
    return {"response": response}

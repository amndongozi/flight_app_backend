import joblib
import pandas as pd

# Load once at startup
pipeline = joblib.load("model/lgbm_model.pkl")

def predict_delay(payload: dict):
    df = pd.DataFrame([payload])
    proba = pipeline.predict_proba(df)[0][1]

    if proba > 0.6:
        risk = "High"
    elif proba > 0.3:
        risk = "Medium"
    else:
        risk = "Low"

    return proba, risk

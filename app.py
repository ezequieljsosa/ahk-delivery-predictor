import os

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from train import MODEL_PATH, train

app = FastAPI(title="predictor")

# Si todavía no hay un modelo entrenado, se entrena uno al arrancar.
artifact = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else train()


class EtaRequest(BaseModel):
    distance_km: float
    items_count: int
    hour: int
    raining: int
    prep_minutes: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/model/version")
def model_version():
    return {"version": artifact["version"], "mae": artifact["mae"]}


@app.post("/predict/eta")
def predict_eta(req: EtaRequest):
    row = pd.DataFrame([req.model_dump()])[artifact["features"]]
    eta = float(artifact["model"].predict(row)[0])
    return {"eta_minutes": round(eta, 1), "model_version": artifact["version"]}

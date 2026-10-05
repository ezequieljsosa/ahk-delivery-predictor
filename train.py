"""Entrena el modelo de ETA con datos sintéticos y lo guarda en MODEL_PATH.

Uso:  python train.py
"""

import os
from datetime import UTC, datetime

import joblib
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from data import FEATURES, TARGET, generate

MODEL_PATH = os.environ.get("MODEL_PATH", "models/eta.joblib")


def train():
    df = generate()
    x_train, x_test, y_train, y_test = train_test_split(df[FEATURES], df[TARGET], random_state=0)
    model = GradientBoostingRegressor(random_state=0).fit(x_train, y_train)
    mae = mean_absolute_error(y_test, model.predict(x_test))

    artifact = {
        "model": model,
        "features": FEATURES,
        "version": datetime.now(UTC).strftime("gbr-%Y%m%d-%H%M%S"),
        "mae": round(float(mae), 2),
    }
    os.makedirs(os.path.dirname(MODEL_PATH) or ".", exist_ok=True)
    joblib.dump(artifact, MODEL_PATH)
    print(f"modelo {artifact['version']} guardado en {MODEL_PATH} (MAE test = {mae:.2f} min)")
    return artifact


if __name__ == "__main__":
    train()

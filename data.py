"""Datos sintéticos de pedidos.

`true_eta` es "la verdad del mundo" que el modelo tiene que descubrir.
Los alumnos de data science no deberían leer esta fórmula: deberían recuperarla desde los datos.
"""

import numpy as np
import pandas as pd

FEATURES = ["distance_km", "items_count", "hour", "raining", "prep_minutes"]
TARGET = "actual_minutes"
PEAK_HOURS = [12, 13, 20, 21]


def true_eta(distance_km, items_count, hour, raining, prep_minutes, rng=None):
    peak = np.isin(hour, PEAK_HOURS) * 8
    eta = prep_minutes + 4 * distance_km * (1 + 0.4 * raining) + 1.2 * items_count + peak
    if rng is not None:
        eta = eta + rng.normal(0, 3, size=np.shape(eta))
    return eta


def generate(n=5000, seed=42):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "distance_km": rng.uniform(0.3, 9, n).round(2),
            "items_count": rng.integers(1, 7, n),
            "hour": rng.integers(11, 24, n),
            "raining": rng.integers(0, 2, n),
            "prep_minutes": rng.choice([15, 25, 30], n),
        }
    )
    df[TARGET] = true_eta(*(df[c].to_numpy() for c in FEATURES), rng=rng).round(1)
    return df

# 002 · Entrenar el modelo

- **Estado:** Implementado
- **Servicio:** predictor
- **Requisitos de sistema:** RS-12

## Historia de usuario

Como data scientist, quiero un script que entrene el modelo con datos sintéticos, para tener un baseline reproducible.

## Requisitos funcionales

- **RF-1** `python train.py` genera 5000 pedidos sintéticos (`data.py`), separa train/test, entrena un `GradientBoostingRegressor` y reporta el MAE de test.
- **RF-2** Guarda en `MODEL_PATH` (por defecto `models/eta.joblib`) un artefacto con `model`, `features`, `version` (`gbr-AAAAMMDD-HHMMSS`) y `mae`.
- **RF-3** Al arrancar, la API carga el artefacto; si no existe, entrena uno nuevo.

## Escenarios de aceptación

1. **Dado** que no existe `eta.joblib`, **cuando** arranca la API, **entonces** entrena, guarda el modelo y responde predicciones.
2. **Dado** datos sintéticos con ruido de 3 minutos, **cuando** se entrena, **entonces** el MAE de test ronda los 3 minutos o menos.

## Fuera de alcance / notas

- La función `true_eta` de `data.py` es "la verdad del mundo" que el modelo debe recuperar. Los alumnos de data science no deberían leerla, sino inferirla de los datos.

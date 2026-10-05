# 003 · Versión del modelo y health

- **Estado:** Implementado
- **Servicio:** predictor
- **Requisitos de sistema:** RS-12

## Historia de usuario

Como operador, quiero saber qué modelo está sirviendo el predictor y si está vivo.

## Requisitos funcionales

- **RF-1** `GET /model/version` responde `{version, mae}` del modelo cargado.
- **RF-2** `GET /health` responde `{status: ok}`.

## Escenarios de aceptación

1. **Dado** un modelo cargado, **cuando** se pide `/model/version`, **entonces** la versión coincide con `model_version` de las predicciones.

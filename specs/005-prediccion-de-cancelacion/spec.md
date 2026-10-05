# 005 · Predecir el riesgo de cancelación

- **Estado:** Propuesto
- **Servicio:** predictor
- **Requisitos de sistema:** RS-12

## Historia de usuario

Como negocio, quiero estimar la probabilidad de que un pedido se cancele, para actuar antes.

## Requisitos funcionales

- **RF-1** `POST /predict/cancel` recibe las mismas features del pedido y devuelve `cancel_probability` (0 a 1) y `model_version`.
- **RF-2** El modelo es un clasificador, con su propio artefacto y su propia versión.
- **RF-3** Se define cómo se obtiene la etiqueta (requiere `order.cancelled`, spec 006 de `order-svc`).

## Escenarios de aceptación

1. **Dado** un pedido de ETA muy alto, **cuando** se predice, **entonces** la probabilidad es mayor que la de un pedido rápido.

## Fuera de alcance / notas

- Hasta que existan cancelaciones reales, se pueden generar etiquetas sintéticas en `data.py`.

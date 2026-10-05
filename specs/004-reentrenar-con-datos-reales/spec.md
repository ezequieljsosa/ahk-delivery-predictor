# 004 · Reentrenar con datos reales

- **Estado:** Propuesto
- **Servicio:** predictor
- **Requisitos de sistema:** RS-12

## Historia de usuario

Como data scientist, quiero entrenar con los pedidos reales del histórico, para que el modelo mejore con el uso.

## Requisitos funcionales

- **RF-1** `train.py --source analytics` lee `orders_history` (solo filas con `actual_minutes`) desde la base `analytics`.
- **RF-2** Reporta el MAE del modelo nuevo y el del modelo actual sobre el mismo conjunto de test.
- **RF-3** Solo reemplaza al modelo vigente si el MAE nuevo es menor.

## Escenarios de aceptación

1. **Dado** 500 pedidos entregados en el histórico, **cuando** se reentrena, **entonces** se imprime la comparación de MAE y se decide si se reemplaza.

## Fuera de alcance / notas

- Excluir del entrenamiento los pedidos cuyo ETA fue de reserva (spec 005 de `order-svc`).

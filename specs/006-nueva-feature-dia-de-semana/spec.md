# 006 · Agregar el día de la semana como feature

- **Estado:** Propuesto
- **Servicio:** predictor
- **Requisitos de sistema:** RS-12

## Historia de usuario

Como data scientist, quiero probar si el día de la semana mejora la predicción.

## Requisitos funcionales

- **RF-1** Se agrega `day_of_week` (0 a 6) al generador de datos, al entrenamiento y a `/predict/eta`.
- **RF-2** El cambio de contrato se coordina con `order-svc`, que debe enviar el campo.
- **RF-3** Se documenta el MAE antes y después.

## Escenarios de aceptación

1. **Dado** el modelo nuevo, **cuando** se compara contra el anterior en el mismo test, **entonces** se informa la mejora (o la falta de ella).

## Fuera de alcance / notas

- Mientras `order-svc` no envíe el campo, el predictor debería aceptar su ausencia con un valor por defecto.

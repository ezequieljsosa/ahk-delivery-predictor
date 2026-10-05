# 001 · Predecir el tiempo de entrega (ETA)

- **Estado:** Implementado
- **Servicio:** predictor
- **Requisitos de sistema:** RS-02

## Historia de usuario

Como servicio de pedidos, quiero consultar online el tiempo estimado de entrega, para mostrárselo al cliente.

## Requisitos funcionales

- **RF-1** `POST /predict/eta` recibe `distance_km`, `items_count`, `hour`, `raining` (0 o 1) y `prep_minutes`, y responde `eta_minutes` (con un decimal) y `model_version`.
- **RF-2** Un body incompleto o con tipos inválidos responde 422 (validación de FastAPI).
- **RF-3** El orden y el nombre de las features salen del artefacto del modelo (`features`), no de código duplicado.

## Escenarios de aceptación

1. **Dado** un pedido de 5 km con lluvia a las 21 hs, **cuando** se predice, **entonces** el ETA es mayor que el de un pedido de 1 km sin lluvia a las 16 hs.
2. **Dado** un body sin `distance_km`, **cuando** se predice, **entonces** responde 422.

## Contrato

```http
POST /predict/eta
{"distance_km": 4.1, "items_count": 2, "hour": 13, "raining": 1, "prep_minutes": 15}

200 OK
{"eta_minutes": 49.3, "model_version": "gbr-20261004-133644"}
```

## Fuera de alcance / notas

- No valida rangos (distancias negativas, `hour` fuera de 0-23).

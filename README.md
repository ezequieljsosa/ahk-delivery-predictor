# ahk-delivery-predictor

Predictor online del tiempo de entrega. Sirve un modelo de scikit-learn que estima los minutos de entrega (ETA) de un pedido. Si no hay un modelo guardado, entrena uno con datos sintéticos al arrancar.

Forma parte de la maqueta de delivery **ahk-delivery**. La arquitectura, los requisitos del sistema y cómo levantar todo con Docker Compose están en [ahk-delivery-infra](https://github.com/ezequieljsosa/ahk-delivery-infra).

- **Stack:** Python 3.12, FastAPI, scikit-learn, pandas
- **Datos:** Archivo `eta.joblib` (con modelo, features, versión y MAE)
- **Imagen:** `ezequieljsosa/ahk-delivery-predictor`

## API

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/predict/eta` | Predice los minutos de entrega |
| GET | `/model/version` | Versión y MAE del modelo cargado |
| GET | `/health` | Estado del servicio |
| GET | `/docs` | Swagger (FastAPI) |

## Ejecutar localmente

Dependencias: ninguna (entrena su propio modelo).

Configuración (variables de entorno): `MODEL_PATH` (default `models/eta.joblib`).

```bash
pip install -r requirements.txt
uvicorn app:app --port 8000
```

El servicio escucha en el puerto **8000**.

Imagen de Docker:

```bash
docker build -t ezequieljsosa/ahk-delivery-predictor .
```

## Specs

Las features están descritas en [`specs/`](specs/README.md) (desarrollo guiado por specs). Las marcadas *Propuesto* son tareas para los alumnos.

## Calidad de código

```bash
pip install pre-commit ruff
pre-commit install                                  # una sola vez: los hooks corren en cada commit
pre-commit run --all-files                          # o: ruff check . && ruff format --check .
```

## Licencia

[MIT](LICENSE)

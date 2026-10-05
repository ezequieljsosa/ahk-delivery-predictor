# AGENTS.md

Guía para quien trabaje en este repositorio, humano o asistente de IA.

## Qué es

`ahk-delivery-predictor`: predictor online del tiempo de entrega de la maqueta ahk-delivery. Sirve un modelo de scikit-learn que estima los minutos de entrega (ETA) de un pedido. Si no hay un modelo guardado, entrena uno con datos sintéticos al arrancar.
El contexto del sistema completo está en [ahk-delivery-infra](https://github.com/ezequieljsosa/ahk-delivery-infra): `docs/requirements.md` (requisitos y diagramas de secuencia) y `docs/architecture.md` (C4).

## Comandos

- Correr: `uvicorn app:app --port 8000`
- Calidad: `pre-commit run --all-files` (o `ruff check . && ruff format --check .`)

## Cómo trabajar: specs primero (SDD)

1. Antes de tocar código, leer el spec de la feature en `specs/NNN-nombre/spec.md`. Si no existe, crearlo (formato en `specs/README.md`).
2. Escribir `plan.md` y `tasks.md` en la carpeta del spec y recién después implementar.
3. Cada escenario de aceptación del spec debe tener su test.
4. Si el cambio altera un contrato entre servicios (REST o eventos), actualizar también los requisitos en [ahk-delivery-infra](https://github.com/ezequieljsosa/ahk-delivery-infra/blob/main/docs/requirements.md) y avisar a los otros repos afectados.
5. Al terminar, marcar el spec como *Implementado*.

## Reglas de este servicio

- El orden y los nombres de las features salen del artefacto (`features`), no se duplican en otro lado.
- Los archivos `*.joblib` no se versionan: se regeneran con `python train.py`.
- `true_eta` en `data.py` es la 'verdad del mundo' del dataset sintético: los alumnos de data science no deberían leerla, sino inferirla de los datos.
- Cada servicio es dueño de su base: nunca acceder a la base de otro servicio.

## Estilo y calidad

- `ruff` (reglas en `ruff.toml`) para estilo, imports, bugs y seguridad; `ruff format` para el formato.
- Identificadores en inglés; mensajes de log y documentación en español.

## Antes de dar por terminada una tarea

- Correr `pre-commit run --all-files`, dejar que los formatters reescriban archivos y revisar el diff.
- Verificar que el spec refleja lo implementado.
- No commitear secretos ni artefactos generados (`target/`, `*.joblib`, `__pycache__/`).

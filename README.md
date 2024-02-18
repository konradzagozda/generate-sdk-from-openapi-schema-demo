# Generate SDK client from openapi.json demo

## Backend App Installation

```sh
poetry install
poetry shell
uvicorn src.main:app --reload
```

### OpenAPI

Documentation is visible at:

- `http://127.0.0.1:8000/openapi.json`
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

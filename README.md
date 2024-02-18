# Generate SDK client from openapi.json demo

Generating SDK clients from openapi.json has the following benefits:

- for each endpoint there is a method generated
- autocompletion and types for all generated methods and their responses
- detection of incompatibilities between components

This demo is inspired by: <https://fastapi.tiangolo.com/advanced/generate-clients/>

## What does it contain?

- example backend application written in FastAPI
- script with steps for generating SDK client
- example usage in typescript react-redux app

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

## Generate SDK client

1. Ensure python app is running on `localhost:8000`
2. `npm install`
3. `npm run fetch-schema`
4. `npm run pre-process-schema`
5. `npm run generate-client`

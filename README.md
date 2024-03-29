# Generate SDK client from openapi.json demo

Generating SDK clients from openapi.json have following benefits:

- for each endpoint there is a method generated
- autocompletion and types for all generated methods and their responses
- necessary code duplication is done via automation
- incompatibilities early detection across your distributed system

This demo is inspired by: <https://fastapi.tiangolo.com/advanced/generate-clients/>

## What does it contain?

- example backend application written in FastAPI
- script with steps for generating SDK client
- example usage of SDK in typescript-node service

## Easy Setup

```sh
./start-demo.sh
```

Check out backend server logs in `nohup.backend` file
Check out node service logs in `nohup.node` file

## Backend App Installation

```sh
poetry install
poetry run uvicorn src.main:app --reload
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

## Node Service Installation

1. `cd node-service`
2. `npm install`
3. `npm run start:dev`

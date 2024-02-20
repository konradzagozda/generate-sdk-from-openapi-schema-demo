#!/usr/bin/env bash
set -x
poetry install
nohup poetry run uvicorn src.main:app --reload > nohup.backend 2>&1 &
echo "PID of nohup poetry run: $!"
sleep 3

npm install
npm run fetch-schema
npm run pre-process-schema
npm run generate-client

cd node-service
npm install
nohup npm run start:dev > ../nohup.node 2>&1 &
echo "PID of nohup npm run start:dev: $!"

echo "use printed PIDs to cleanup the processes later with kill -9 PID"
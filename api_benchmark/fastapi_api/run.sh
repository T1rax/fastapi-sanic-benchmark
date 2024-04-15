#!/usr/bin/env bash

set -e

gunicorn api_benchmark.fastapi_api.main:app --bind 0.0.0.0:8000 --workers 3 --worker-class uvicorn.workers.UvicornWorker --log-file=- --access-logfile=- --error-logfile=-
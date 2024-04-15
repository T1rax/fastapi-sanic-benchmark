#!/usr/bin/env bash

set -e

sanic api_benchmark.sanic_api.server:app --host=0.0.0.0 --port=8000 --workers=3
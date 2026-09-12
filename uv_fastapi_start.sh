#!/bin/bash

set -eu


# Activate virtualenv && run serivce
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

VENV=".venv"
# VENV=".test_venv"

# Python 3.11.7 with Window
if [ -d "$VENV/bin" ]; then
    source $VENV/bin/activate
else
    source $VENV/Scripts/activate
fi

export PYTHONDONTWRITEBYTECODE=1

# uvicorn 실행 시 --reload 옵션을 주어야 소스 변경을 감지합니다.
# uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
uv run uvicorn app.main:app --reload --host=0.0.0.0 --port=8001 --workers 1

# gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8001 --workers 1
# gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8001 --workers 4
#!/bin/bash

set -eu

# uvicorn 실행 시 --reload 옵션을 주어야 소스 변경을 감지합니다.
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
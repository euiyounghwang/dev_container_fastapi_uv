FROM python:3.11-slim

# 시스템 필수 패키지 및 uv 설치
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# 2. Copy the rest of the application source code
COPY ../ .

# uv를 사용해 가상환경 생성 및 경로 설정
ENV VIRTUAL_ENV=/workspace/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 소스 동기화 후 devcontainer 안에서 패키지를 설치하므로 
# Dockerfile 단계에서는 최소한의 환경만 정의합니다.
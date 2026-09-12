# -------------------------------------------------------------
# Stage 1: 의존성 설치 및 가상환경 빌드 (캐시 활용)
# -------------------------------------------------------------
FROM python:3.11-slim AS builder

WORKDIR /workspace

# uv 바이너리 가져오기 및 링크 모드 설정
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_LINK_MODE=copy

# 패키지 명세 파일만 먼저 복사하여 레이어 캐시 활성화
# COPY pyproject.toml uv.lock* ./
COPY ../. .

# 도커 빌드 캐시를 활용하여 초고속 의존성 싱크 (프로젝트 자체는 제외)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# -------------------------------------------------------------
# Stage 2: 최종 Dev Container 개발 레이어
# -------------------------------------------------------------
FROM python:3.11-slim AS runtime

# FastAPI 기본 포트 오픈
EXPOSE 8000

WORKDIR /workspace

# uv 바이너리 및 빌드된 가상환경(.venv) 복사
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY --from=builder /workspace/.venv ./.venv
COPY --from=builder /workspace .

# 가상환경 활성화를 위한 환경변수 설정
ENV VIRTUAL_ENV=/workspace/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# 빌드 셸을 bash로 변경
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
FROM python:3.12-slim-bookworm AS base

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app
COPY main.py pyproject.toml uv.lock* ./
COPY app ./app
RUN uv sync --frozen --no-dev

# Copy Prisma schema and generate client
COPY prisma ./prisma
RUN uv run prisma generate

FROM base AS dev
COPY . .
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.13-slim@sha256:026dd417a88d0be8ed5542a05cff5979d17625151be8a1e25a994f85c87962a5

COPY --from=ghcr.io/astral-sh/uv:latest@sha256:031ddbc79275e351a43cbb66f64d8cd314cc78c3878898f4ab4f147b092e8e2d /uv /uvx /bin/

ENV APP_DIR=/app
ENV TZ=Asia/Singapore
ENV PYTHONPATH=$APP_DIR/src
ENV UV_CACHE_DIR=/home/user/.cache/uv
ENV PYTHONUNBUFFERED=TRUE
ENV CACHE_UID=1000
ENV CACHE_GID=1000

# Speed up container start time https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
ENV UV_COMPILE_BYTECODE=1

# uv: Don't link packages to the mounted cache on the host (which will not be present in the final image). Instead, copy packages to the container
ENV UV_LINK_MODE=copy

# Ensure that the `python` command uses the venv
ENV PATH="$APP_DIR/.venv/bin:$PATH"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg mp3val flac xdg-utils git && \
    rm -rf /var/lib/apt/lists/*

# Run the container as a non-root user
RUN useradd -ms /bin/bash --user-group -l -u ${CACHE_UID} user

USER user

WORKDIR /app

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$CACHE_UID,gid=$CACHE_GID \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen

FROM python:3.13.11-slim-bookworm AS camino_base
SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

ARG UID
ARG GID

RUN <<EOF
    export DEBIAN_FRONTEND=noninteractive &&
    apt-get update &&
    apt-get install --yes --no-install-recommends \
        procps \
        ca-certificates \
        curl \
        gnupg \
        locales \
        tzdata \
        build-essential \
        libpq-dev &&
    sed -i '/en_GB.UTF-8/s/^# //g' /etc/locale.gen && locale-gen &&
    apt-get autoremove --yes && apt-get clean --yes && rm -rf /var/lib/apt/lists/*
EOF

ENV LANG=en_GB.UTF-8
ENV LC_ALL=en_GB.UTF-8

COPY --from=ghcr.io/astral-sh/uv:0.9.16 /uv /uvx /bin/

# Create user with the specified UID/GID
RUN set -eux; \
    if ! getent group ${GID}; then \
    groupadd -g ${GID} appgroup; \
    else \
    GROUPNAME=$(getent group ${GID} | cut -d: -f1); \
    fi; \
    useradd -u ${UID} -g ${GID} -s /bin/bash -d /app -M appuser; \
    mkdir -p /app && chown -R ${UID}:${GID} /app

WORKDIR /app

COPY --chown=${UID}:${GID} ./pyproject.toml ./uv.lock /app/
RUN chown -R ${UID}:${GID} /app

RUN uv venv

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --no-dev

COPY --chown=${UID}:${GID} ./src/app/ /app/app/

# Install the project itself so console-script entry points (e.g. prod-dashboard) are created
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# Ensure uv-managed virtualenv is in PATH
ENV PATH="/app/.venv/bin:$PATH"

FROM camino_base AS camino_bronze
ENTRYPOINT ["gunicorn", "app.main:server", "--bind", "0.0.0.0:8050"]

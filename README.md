# Camino Pharmacy Dashboard

A small demonstrator [Plotly Dash](https://plotly.com/dash/) dashboard for pharmacists served by the [RADIX](https://radix.antibiotics.help) [Camino datalake](https://radix.antibiotics.help/foundations/camino-frances).

[![Tests](https://github.com/SAFEHR-data/camino-pharmacy-dashboard/actions/workflows/tests.yaml/badge.svg)](https://github.com/SAFEHR-data/camino-pharmacy-dashboard/actions/workflows/tests.yaml)
[![Linting](https://github.com/SAFEHR-data/camino-pharmacy-dashboard/actions/workflows/linting.yaml/badge.svg)](https://github.com/SAFEHR-data/camino-pharmacy-dashboard/actions/workflows/linting.yaml)
[![uv](https://img.shields.io/badge/uv-gray?logo=uv)](https://docs.astral.sh/uv)
[![prek](https://img.shields.io/badge/prek-gray?logo=prek)](https://github.com/j178/prek)
[![ruff](https://img.shields.io/badge/ruff-gray?logo=ruff)](https://docs.astral.sh/ruff)

## Development

For local development, set up a new [`uv`](https://docs.astral.sh/uv/) virtual environment (you'll need to do this once, then every time the dependencies in [`pyproject.toml`](./pyproject.toml) change).

```bash
uv venv
source .venv/bin/activate
uv sync
```

Then, start the development server with:

```bash
source .venv/bin/activate
dev-dashboard # starts up the development dashboard server (with callback graph etc)
```

The development server will be available at [`http://localhost:8050`](http://localhost:8050) and should show the callback graph.
Every time you make a change to the code, the server should automatically reload and reflect your changes.

You might (for some reason) need to start the production version of the server locally outside of Docker for testing and development.
This is:
```bash
source .venv/bin/activate
gunicorn app.main:server --bind :8050
```

### Development workflow

Changes to the codebase by pull request.
And check the linters and tests pass before merging.

Linters are run with [`prek`](./prek.toml).
```bash
uv run prek --all-files
```
or
```bash
uv sync
prek --all-files
```

Tests are run with `pytest`.

> [!NOTE]
> In order to run the selenium tests, you need a webdriver.
> Either install one, e.g.
> ```
> brew install --cask chromedriver
> ```
>
> ... or allow prerelease versions so that you can grab the latest selenium (4.6 or newer).
> ```
> uv sync --prerelease=if-necessary
> ```
>
> The very latest `dash[testing]` version (currently a prerelease) depends on a newer selenium 4.6+ version which will automatically download a webdriver for you.
> When `dash` release their next stable version we can delete this whole note and disallow prerelease versions (regenerate `uv.lock`).

## Production

Running on GAE13.
Code at `/gae/camino-pharmacy-dashboard`.
Docker containers called `camino-pharmacy-dashboard`.
The deployed application relies on the Camino datalake being available.

To redeploy you'll need to create an environment file.
Copy `.env.example` to `.env` and fill in the values.

Then deploy with:

```
docker compose up -d --build
```
See the [`Dockerfile`](./Dockerfile) and [`docker-compose.yml`](./docker-compose.yml) for details.

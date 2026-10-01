# Camino Pharmacy Dashboard

A small demonstrator `dash` dashboard for pharmacists served by the Camino datalake.

## Development

For local development, set up a new `uv` virtual environment (you'll need to do this once, then every time the dependencies in [`pyproject.toml`](./pyproject.toml) change).

```bash
uv venv
source .venv/bin/activate
uv sync
```

Then, start the development server with:

```bash
source .venv/bin/activate
dev-dashboard # starts up the development dashboard server (with callback graph etC)
```

The development server will be available at [http://localhost:8050](http://localhost:8050) and should show the callback graph.
Every time you make a change to the code, the server should automatically reload and reflect your changes.

Changes to the codebase by pull request.
And check the linters and tests pass before merging.

Linters are run with [`prek`](./.pre-commit-config.yaml).
```
uv run prek --all-files
```
or
```
uv sync
prek --all-files
```

Tests are run with `pytest`.

> [!NOTE]
> In order run the selenium tests, you need a webdriver.
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

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

<!---
Changes to the codebase by pull request.
And check the linters pass with [`prek`](./.pre-commit-config.yaml) before merging.

--->

```
docker compose up -d --build
```
See the [`Dockerfile`](./Dockerfile) and [`docker-compose.yml`](./docker-compose.yml) for details.

from .config import settings
import duckdb


def connect_to_camino() -> duckdb.DuckDBPyConnection:
    """Connect to the Camino datalake

    Uses `duckdb.connect` with a secret attachment string containing username
    and password for the pharmacy dashboard user. (Which is a read-only user.)
    """
    cc = duckdb.connect()  # just need any old duckdb
    cc.execute(
        f"SET http_proxy='{settings.HTTP_PROXY}';"
    )  # proxy to install extensions
    cc.install_extension("ducklake")
    cc.install_extension("postgres")
    cc.execute(settings.CAMINO_ATTACH.get_secret_value())  # attach to camino datalake
    return cc

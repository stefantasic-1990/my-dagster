from dagster import Definitions
from resources import SFTPResource
from assets import sftp_pokemon_csv
from jobs import ingest_source_data

defs = Definitions(
    assets=[sftp_pokemon_csv],
    jobs=[ingest_source_data],
    resources={
        "source_sftp": SFTPResource(hostname="dagster-sftp", username="dagster_user", password="dagster_password")
    },
)
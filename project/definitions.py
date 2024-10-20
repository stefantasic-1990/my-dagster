from dagster import Definitions, define_asset_job
from resources import SFTPResource
from assets import sftp_pokemon_csv

ingest_source_data = define_asset_job(
    name="ingest_source_data",
    selection=["sftp_pokemon_csv"]
)

defs = Definitions(
    assets=[sftp_pokemon_csv],
    jobs=[ingest_source_data],
    resources={
        "source_sftp": SFTPResource(hostname="dagster-sftp", username="dagster_user", password="dagster_password")
    },
)
from dagster import Definitions, define_asset_job
from resources import SFTPResource
from assets import source_sftp_csv

ingest_source_data = define_asset_job(
    name="ingest_source_data", selection="source_sftp_csv"
)

defs = Definitions(
    assets=[source_sftp_csv],
    jobs=[ingest_source_data],
    resources={
        "source_sftp": SFTPResource(hostname="dagster-source-sftp", username="dagster-user", password="dagster-password")
    },
)
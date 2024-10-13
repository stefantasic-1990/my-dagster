from dagster import Definitions, define_asset_job
from resources import SFTPResource
from assets import source_json_sftp

ingest_source_data = define_asset_job(
    name="ingest_source_data", selection="source_json_sftp"
)

defs = Definitions(
    assets=[source_json_sftp],
    jobs=[ingest_source_data],
    resources={
        "sftp_source": SFTPResource(host="dagster-source-sftp", username="dagster-user", password="dagster-password")
    },
)
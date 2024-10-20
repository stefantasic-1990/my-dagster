from dagster import define_asset_job

ingest_source_data = define_asset_job(
    name="ingest_source_data",
    selection=["sftp_pokemon_csv"]
)
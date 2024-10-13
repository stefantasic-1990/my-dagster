from dagster import asset
from resources import SFTPResource

@asset
def source_json_sftp(sftp_source: SFTPResource) -> list:
    conn = sftp_source.connect()
    file_list = conn.listdir("/incoming/")

    return file_list
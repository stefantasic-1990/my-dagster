from dagster import asset
from resources import SFTPResource

@asset
def source_json_sftp(sftp_source: SFTPResource) -> None:
    file_list = sftp_source.listdir("/incoming/")
    return file_list
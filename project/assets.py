from dagster import asset, MaterializeResult
from resources import SFTPResource

@asset
def source_json_sftp(sftp_source: SFTPResource) -> MaterializeResult:
    conn = sftp_source.connect()
    file_list = conn.listdir("/incoming/")

    return MaterializeResult(
        metadata={
            "files": str(file_list)
        }
    )
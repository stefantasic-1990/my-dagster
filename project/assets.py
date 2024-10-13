from dagster import asset, MaterializeResult
from resources import SFTPResource

@asset
def source_sftp_csv(source_sftp: SFTPResource) -> MaterializeResult:
    files = source_sftp.get_file_list('/incoming/')

    return MaterializeResult(
        metadata={
            "files": str(files)
        }
    )
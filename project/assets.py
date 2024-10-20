from dagster import asset, Output
from resources import SFTPResource

@asset
def sftp_pokemon_csv(source_sftp: SFTPResource) -> Output:
    
    files = source_sftp.get_file_list('/incoming/')

    return Output(
        value=files,
        metadata={
            "files": str(files)
        }
    )

# @asset
# def mysql_pokemon_table(files: list, source_sftp: SFTPResource) -> MaterializeResult:

#     archive_directory = '/archive/'
#     for file in files:
#         # Logic to archive the file (e.g., move it)
#         source_sftp.archive_file(file, archive_directory)

#     return MaterializeResult(
#         metadata={
#             "archived_files": str(files)
#         }
#     )
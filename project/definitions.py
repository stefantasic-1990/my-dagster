from dagster import Definitions
from resources import SFTPResource

defs = Definitions(
    resources={
        "sftp_source": SFTPResource(host="dagster-source-sftp", username="dagster-user", password="dagster-password")
    },
)
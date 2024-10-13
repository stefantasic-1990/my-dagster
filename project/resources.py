from dagster import ConfigurableResource
from paramiko import SSHClient

class SFTPResource(ConfigurableResource):
    host: str
    username: str
    password: str

    def connect(self, host: str, username: str, password: str):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host=host, port=22, username=username, password=password)
        client = ssh.open_sftp()

        return client
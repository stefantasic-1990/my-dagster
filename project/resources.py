import paramiko
from dagster import ConfigurableResource

class SFTPResource(ConfigurableResource):
    hostname: str
    username: str
    password: str

    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=22, username=self.username, password=self.password)
        client = ssh.open_sftp()

        return client
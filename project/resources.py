import paramiko
from dagster import ConfigurableResource

class SFTPResource(ConfigurableResource):
    hostname: str
    username: str
    password: str

    def get_file_list(self, dir):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=22, username=self.username, password=self.password)
        files = ssh.open_sftp().listdir(f"{dir}")
        ssh.close()

        return files

    def get_file(self, path):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=22, username=self.username, password=self.password)
        sftp = ssh.open_sftp()
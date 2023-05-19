# region				-----External Imports-----
import glob
import os
# endregion


def docker_swarm_secrets_import() -> None:
    for secret in glob.glob('/run/secrets/*'):
        secret_name=secret.split('/')[-1]
        secret_value=open(secret).read().rstrip('\n')
        os.environ[secret_name] = secret_value
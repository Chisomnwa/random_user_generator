import boto3
from airflow.models import Variable


def session():
    session = boto3.Session(
            aws_access_key_id=Variable.get('access_key'),
            aws_secret_access_key=Variable.get('secret_key'),
            region_name='eu-central-1'
        )
    return session

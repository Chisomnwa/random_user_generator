# Import the required airflow modules
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime

from random_users.get_data import get_shape

# Create default arguments
default_args = {
    'owner': 'chisom',
    'start_date': datetime(2024, 11, 20),
    'retries': 3,
    'retry_delay': timedelta(seconds=3),
    'execution_timeout': timedelta(minutes=10),
}

# Instantiate a DAG
dag = DAG(
    dag_id="random_user_generator",
    default_args=default_args,
    default_view="graph",
    tags=["generate_users"],
    description='returning random users',
    schedule_interval="0 0 * * *",
    catchup=False
)

convert_profiles = PythonOperator(
    dag=dag,
    task_id='convert_profiles',
    python_callable=get_shape
    )

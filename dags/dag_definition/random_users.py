# Import the required airflow modules
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime

from utils.extract_data import extract_selected_columns
from utils.transfer_to_s3 import upload_to_s3

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

# Create a Python operator object that calls function that extracts
# the data from the API
# Extracts the required columns and then converts it to a pandas dataframe
convert_profiles = PythonOperator(
    dag=dag,
    task_id='convert_profiles',
    python_callable=extract_selected_columns
    )

# Create a Python operator object that calls the function that loads data to s3
load_data_to_s3 = PythonOperator(
    dag=dag,
    task_id='load_data',
    python_callable=upload_to_s3
)

# Specify the task dependencies
convert_profiles >> load_data_to_s3

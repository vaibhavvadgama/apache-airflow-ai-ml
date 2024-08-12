from airflow import DAG
from datetime import datetime
import os
import pprint
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

def _print_environment_variables():
    print(os.environ)
    pprint.pprint(dict(os.environ), width = 2)

with DAG(
    dag_id="airflow_env_variables_dag",
    start_date=datetime(2024,1,1),
    schedule_interval='@daily',
    catchup=False
):
    print_environment_variables = PythonOperator(
        task_id = 'print_environment_variables',
        python_callable=_print_environment_variables
    )

    test_database_connection = PostgresOperator(
        task_id='test_database_connection',
        postgres_conn_id='my_postgres',
        sql='SELECT 1;'
    )

    print_environment_variables >> test_database_connection
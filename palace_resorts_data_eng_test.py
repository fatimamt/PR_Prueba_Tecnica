from datetime import timedelta
from pendulum import datetime, timezone
from pathlib import Path

# DAG object
from airflow import DAG

# Operators
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.task_group import TaskGroup

from PalaceResorts.utils import excel_to_csv

BASE_PATH = Path(__file__).parent
DEFAULT_ARGS = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'concurrency': 9
}
DAG_ID = 'palace_resorts_data_eng_test'


with DAG(
    dag_id=DAG_ID,
    schedule_interval='0 10 * * *',
    start_date=datetime(2023, 12, 1, tz=timezone('Etc/GMT+6')),

    catchup=False,
    default_args=DEFAULT_ARGS,
    template_searchpath=str(BASE_PATH)
):
    excel_csv = PythonOperator(
        task_id='CONVERT_EXCEL_TO_DF',
        python_callable=excel_to_csv,
        op_kwargs={
            'filename': '/files/MATRIZ_DATA_TEAM.xlsx',
            'path': str(BASE_PATH)
        }
    )

    CSV_FILES = '{{ task_instance.xcom_pull(task_ids="CONVERT_EXCEL_TO_DF") }}'

    create_tables = MySqlOperator(
        task_id=f"CREATE_TABLES",
        sql="/queries/create_tables.sql",
        mysql_conn_id='mysql_db',
    )

    csv_mysql = MySqlOperator(
        task_id=f"UPLOAD_TO_MYSQL",
        sql="/queries/load_data.sql",
        mysql_conn_id='mysql_db',
        params={
            'filepath': str(BASE_PATH) + 'files/MATRIZ_DE_ADYACENCIA',
            'check_name': 'MATRIZ_DE_ADYACENCIA'
        }
    )

    excel_csv >> create_tables >> csv_mysql

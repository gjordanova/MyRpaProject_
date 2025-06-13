import os, sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from airflow import DAG
from airflow.operators.python import PythonOperator
from config.settings import BASE_URL
from src.utils.helpers import get_output_paths
from src.scrapers.books_scraper import scrape_books
from src.processors.data_processor import process_data
from src.validators.data_validator import validate_data
from src.reporters.report_generator import generate_report

paths = get_output_paths()
raw_path = paths['raw']
processed_path = paths['processed']
report_dir = paths['report']

default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='data_pipeline',
    default_args=default_args,
    start_date=datetime(2025, 6, 13),
    schedule_interval='@daily',
    catchup=False,
    tags=['example'],
) as dag:

    t1 = PythonOperator(
        task_id='scrape_books',
        python_callable=scrape_books,
        op_kwargs={'base_url': BASE_URL, 'output_path': raw_path},
    )
    t2 = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        op_kwargs={'input_path': raw_path, 'output_path': processed_path},
    )
    t3 = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
        op_kwargs={'input_path': processed_path},
    )
    t4 = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report,
        op_kwargs={'input_path': processed_path, 'report_dir': report_dir},
    )

    t1 >> t2 >> t3 >> t4

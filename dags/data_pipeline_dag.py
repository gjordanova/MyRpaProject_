import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.settings import BASE_URL
from src.scrapers.books_scraper import scrape_books
from src.processors.data_processor import process_data
from src.validators.data_validator import validate_data
from src.reporters.report_generator import generate_report

default_args = {"owner": "you", "depends_on_past": False, "retries": 1}

with DAG(
    dag_id="data_pipeline",
    default_args=default_args,
    description="Scrape → Process → Validate → Report",
    start_date=datetime(2025, 6, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["example"],
) as dag:

    scrape = PythonOperator(
        task_id="scrape_books",
        python_callable=scrape_books,
        op_kwargs={"base_url": BASE_URL},
    )

    process = PythonOperator(
        task_id="process_data",
        python_callable=process_data,
        op_kwargs={"df": "{{ ti.xcom_pull(task_ids='scrape_books') }}"},
    )

    validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
        op_kwargs={"df": "{{ ti.xcom_pull(task_ids='process_data') }}"},
    )

    report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
        op_kwargs={"df": "{{ ti.xcom_pull(task_ids='validate_data') }}"},
    )

    scrape >> process >> validate >> report

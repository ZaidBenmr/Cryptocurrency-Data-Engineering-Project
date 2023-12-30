from datetime import datetime, timedelta
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from storage_process_func import read_clean_scraped_data
 
with DAG("job_2_dag", start_date = datetime(2023, 11, 9), schedule_interval=None, catchup=False) as dag:
    
    store_process_task = PythonOperator(
        task_id='store_process_task',
        python_callable=read_clean_scraped_data
    )

    store_process_task

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from scraper_coinmarket import scrape_data
 
#def _scrape_data(ti):
#    df = pd.DataFrame(scrape_data())
#    ti.xcom_push(key='dataframe', value=df)


with DAG("job_1_scrape_cryptobalance", start_date = datetime(2023, 11, 26), schedule_interval=timedelta(seconds=10), catchup=False) as dag:
    
    # Define the tasks
    scraper_produce_task = PythonOperator(
        task_id='scraper_produce_task',
        python_callable=scrape_data
    )

    # Define the tasks
    #index_data_task = PythonOperator(
    #   task_id='index_data_task',
    #    python_callable=index_data,
    #    op_args=["Crypto_balance","my_index"]
    #)

    scraper_produce_task #>> index_data_task

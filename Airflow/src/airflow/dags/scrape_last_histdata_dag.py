from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from scraper_historicaldata import scrape_and_produce_data
 
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 29, 0, 10),  # Start date is set to 29th December 2023 at 12:10 AM
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG("job_scrape_historical_data", default_args=default_args, schedule_interval=timedelta(days=1), catchup=False) as dag:
    
    # Define the tasks
    scraper_BTC_data = PythonOperator(
        task_id='scraper_BTC_data',
        python_callable=scrape_and_produce_data,
        op_args=["BTC-USD","btcsnapshots"]
    )
    scraper_BNB_data = PythonOperator(
        task_id='scraper_BNB_data',
        python_callable=scrape_and_produce_data,
        op_args=["BNB-USD","bnbsnapshots"]
    )
    scraper_ETH_data = PythonOperator(
        task_id='scraper_ETH_data',
        python_callable=scrape_and_produce_data,
        op_args=["ETH-USD","ethsnapshots"]
    )
    scraper_XRP_data = PythonOperator(
        task_id='scraper_XRP_data',
        python_callable=scrape_and_produce_data,
        op_args=["XRP-USD","xrpsnapshots"]
    )
    scraper_AAVE_data = PythonOperator(
        task_id='scraper_AAVE_data',
        python_callable=scrape_and_produce_data,
        op_args=["AAVE-USD","aavesnapshots"]
    )
    scraper_ADA_data = PythonOperator(
        task_id='scraper_ADA_data',
        python_callable=scrape_and_produce_data,
        op_args=["ADA-USD","adasnapshots"]
    )
    scraper_BCH_data = PythonOperator(
        task_id='scraper_BCH_data',
        python_callable=scrape_and_produce_data,
        op_args=["BCH-USD","bchsnapshots"]
    )
    scraper_DOGE_data = PythonOperator(
        task_id='scraper_DOGE_data',
        python_callable=scrape_and_produce_data,
        op_args=["DOGE-USD","dogesnapshots"]
    )
    scraper_DOT_data = PythonOperator(
        task_id='scraper_DOT_data',
        python_callable=scrape_and_produce_data,
        op_args=["DOT-USD","dotsnapshots"]
    )
    scraper_TRX_data = PythonOperator(
        task_id='scraper_TRX_data',
        python_callable=scrape_and_produce_data,
        op_args=["TRX-USD","trxsnapshots"]
    )

    [scraper_BTC_data, scraper_BNB_data, scraper_ETH_data, scraper_XRP_data, scraper_AAVE_data,
     scraper_ADA_data, scraper_BCH_data, scraper_DOGE_data, scraper_DOT_data, scraper_TRX_data]


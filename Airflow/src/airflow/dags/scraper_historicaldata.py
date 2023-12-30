from bs4 import BeautifulSoup as bs
from selenium import webdriver
from confluent_kafka import Producer
import json
from datetime import datetime

def scrape_and_produce_data(crypto_name, index_name):

    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=option)

    URL = f"https://finance.yahoo.com/quote/{crypto_name}/history"

    # Use the driver to navigate the page
    driver.get(URL)

    # Get the page source after scrolling
    page_source = driver.page_source

    # Close the driver
    #driver.quit()
    soup1 = bs(page_source,'html.parser')
    row  = soup1.find('table', attrs={'class' : 'W(100%) M(0)',
                                            'data-test' : 'historical-prices'}) \
                        .find('tbody') \
                        .find('tr')


    values       = row.find_all('td')
    date_val     = values[0].get_text().strip()
    open_val     = values[1].get_text().strip()
    high_val     = values[2].get_text().strip()
    low_val      = values[3].get_text().strip()
    close_val    = values[4].get_text().strip()
    adjclose_val = values[5].get_text().strip()
    volume_val   = values[6].get_text().strip()

    # Get the current time
    now = datetime.now()
    scraping_time = now.strftime("%H:%M:%S")
    
    data = {'Date': date_val, 'Time': scraping_time, 'Open': open_val, 'High': high_val, 'Low': low_val, 'Close': close_val, 'Adj Close': adjclose_val, 'Volume': volume_val}

    # Create a Kafka producer configuration
    producer_config = {
        'bootstrap.servers': '192.168.11.107:9092',  # Replace with your Kafka broker address
        'client.id': 'btc-snapshots-producer'
    }
    
    # Create a Kafka producer instance
    producer = Producer(producer_config)

    # Serialize the data to JSON
    data_json = json.dumps(data).encode('utf-8')

    # Convert the DataFrame to a JSON format and send to Kafka
    producer.produce(index_name, value=data_json)

    # Wait for any outstanding messages to be delivered and delivery reports to be received
    producer.flush()

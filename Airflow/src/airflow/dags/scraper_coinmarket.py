import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from confluent_kafka import Producer
import time
from datetime import datetime

def scrape_data():
    
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--disable-gpu')

    #s = Service('chromedriver/chromedriver.exe')

    driver = webdriver.Chrome(options=option)

    URL = "https://coinmarketcap.com/"

    # Use the driver to navigate the page
    driver.get(URL)

    time.sleep(5)

    # Automatically scroll the page
    scroll_pause_time = 0.5  # Pause between each scroll
    last_height = driver.execute_script("return window.screen.height;")  # Browser window height
    i = 1
    while i <= 14 :
        # Scroll down
        driver.execute_script("window.scrollTo(0, {height}*{i});".format(height=last_height, i=i))
        i += 2
        time.sleep(scroll_pause_time)


    # Get the page source after scrolling
    page_source = driver.page_source

    # Close the driver
    driver.quit()

    soup1 = bs(page_source,'html.parser')
    rows  = soup1.find('table', attrs={'class' : 'sc-66133f36-3 etbEmy cmc-table'}) \
                    .find('tbody') \
                    .find_all('tr')

    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    l = list()

    for row in rows :
        values    = row.find_all('td')
        name      = values[2].find('p').get_text().strip()
        price     = values[3].find('span').get_text().strip()
        onehour   = values[4].find('span').get_text().strip()
        oneday    = values[5].find('span').get_text().strip()
        sevendays = values[6].find('span').get_text().strip()
        marketcap = values[7].find_all('span')[1].get_text().strip()
        volume    = values[8].find_all('p')[0].get_text().strip()
        supply    = values[9].find('p').get_text().strip()
        
        data = {'datetime': current_datetime, 'name':name, 'price': price, 'onehour': onehour, 'oneday': oneday, 'sevendays': sevendays, 
                'marketcap': marketcap, 'Volume': volume, 'Supply': supply}
        l.append(data)
    
    df = pd.DataFrame(l)
    #print(df.head(10))
    # Create a Kafka producer configuration
    producer_config = {
        'bootstrap.servers': '192.168.11.107:9092',  # Replace with your Kafka broker address
        'client.id': 'pandas-producer'
    }
    # Create a Kafka producer instance
    producer = Producer(producer_config)

    # Convert the DataFrame to a JSON format and send to Kafka
    for _, row in df.iterrows():
        message = row.to_json()
        producer.produce('cryptobalance', value=message)
        
    # Wait for any outstanding messages to be delivered and delivery reports to be received
    producer.flush()

    return "Data has been pushed successfully"



if __name__ == "__main__":
    scrape_data()
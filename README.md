<div align="center">
  <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/16ff8095-6f1b-4c0b-b9ea-e969c5633e84" alt="Banner" width="780">
  
  <div id="user-content-toc">
    <ul>
      <summary><h1 style="display: inline-block;"> Cryptocurrency Data Analysis 📈</h1></summary>
    </ul>
  </div>
  
  <p>👨‍🔧👷 Data Engineering project Using Web Scraping & Kafka & MongoDB & Elasticsearch & Power BI & Angular JS </p>
    🌀
    ☄️
    🌀
</div>
<br>

<div align="center">
      <a href="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white">
      </a>
      <img src="https://img.shields.io/github/stars/hamagistral/DataEngineers-Glassdoor?color=blue&style=social"/>
</div>

## 📝 Table of Contents

1. [ Project Overview ](#introduction)
2. [ Dashboard ](#dashboard)
3. [ Project Architecture ](#arch)
4. [ Web Scraping ](#webscraping)
5. [ Installation ](#installation)
6. [ Contact ](#contact)
<hr>


<a name="introduction"></a>
## 🔬 Project Overview :

### 💾 Dataset : 
The dataset used contains all historical data between 01/01/2015 and 14/12/2023 for 10 cryptocurrency. In our project, we focus on Bitcoin, Binance, Ethereum, XRP, Bitcoin Cash, AAVE, Cardano, Polkadot, Dogecoin, Tron.
The dataset includes the following columns:

| **Column** | **Description** |
| :--------------- |:---------------| 
| **Date** |  The timestamp indicating the date and time of a particular data point in the dataset. It represents when the corresponding financial data was recorded. The format of the date is : yyyy-MM-dd |  
| **Open** | The opening price of a cryptocurrency at the beginning of a trading period. |
| **High**   |  The highest price of a cryptocurrency during a specific time period (day).  |
| **Low**   |  The lowest price of a cryptocurrency during a specific time period.  |
| **Close**   |  The closing price of a cryptocurrency at the end of a trading period.  |
| **Adj Close**   |   The adjusted closing price of a cryptocurrency. It accounts for any corporate actions (e.g., stock splits, dividends) that may affect the closing price.  |
| **Volume**   |  The total quantity of a cryptocurrency traded during a specific time period.  |


### 🎯 Goal :

This is an end-to-end Data Engineering project where I created an ETL data pipeline to extract cryptocurrency data from various sources, transform this data, and load it into an on-premise NoSQL Database (MongoDB). I then indexed this data into an Elasticsearch search engine to visualize insights using Power BI and AngularJS.

The Power BI dashboard contains graphic representations of the crypto data and provides analyses that can aid in decision-making strategies. The AngularJS dashboard is oriented towards statistical analysis and visualizing forecasting graphs for each coin.

Additionally, I used the transformed data to train an LSTM forecasting model to predict future closing prices for every coin. Subsequently, I deployed the models on a Django web server using Django REST Framework.


### 🧭 Steps :

In our way to implemente this project, we've passed with the following steps : 
#### 1- The project begins with the web scraping of cryptocurrency historical data from <a href="https://finance.yahoo.com/quote/ETH-USD/history" target="_blank">Yahoo finance</a> website. The collected data includes date, high, low, open, close, adj close, and volume.
#### 2- I ingested the raw data into Kafka to deliver real time streaming data to a MongoDB collection. The data quality checks and transformations is performed before storing into MongoDB.
#### 3- I created a Logstash pipeline to capture changes in the transformed data and indexed it from MongoDB into Elasticsearch for visualization.
#### 4- Using the Power BI tool, I created key performance indicators (KPIs) and performed analytics on the cleaned cryptocurrency data.
#### 5- Utilizing Jupyter, pandas, and TensorFlow, I trained an LSTM forecasting model for each coin using the data from Elasticsearch. Each trained model for each coin was deployed into a Django REST API.
#### 6- In the Django REST API, I created statistical analytics from the historical data stored in Elasticsearch using APIs.
#### 7- I used AngularJS to visualize the statistical analysis and forecasting graphs, providing a dahsboard interface for exploring the data.
#### 8- Finally, I set up an Airflow environment using Docker to orchestrate the entire workflow. This included scheduling scraping jobs to run daily, ensuring that the data pipeline operates smoothly and efficiently.


<a name="dashboard"></a>
## 📊 Dashboard
### Power BI
<div style="display: flex; flex-wrap: wrap; justify-content: center;" align="center">
    <div style="display: flex; flex-direction: row;">
        <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/16ff8095-6f1b-4c0b-b9ea-e969c5633e84" alt="Banner" width="500">
        <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/060ec898-81f6-4057-8e5a-12338f7a39c0" alt="Banner" width="500">
    </div>
    <div style="display: flex; flex-direction: row;">
        <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/c707d26a-1dc8-4e02-8b2f-b3b00ce9c5bc" alt="Banner" width="500">
        <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/1176f3f0-ea49-41a8-9e99-7fcd6c3a3947" alt="Banner" width="500">
    </div>
</div>

### Angular Dashboard
<div style="display: flex; flex-wrap: wrap; justify-content: center;" align="center">
    <div style="display: flex; flex-direction: row;">
        <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/0c48f59b-c157-42d9-8304-18f4080e9e99" alt="Banner" width="500" height="250">
        <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/6a132813-18a0-443d-850c-b66b0139a2be" alt="Banner" width="500" height="250">
    </div>
    <div style="display: flex; flex-direction: row;">
        <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/df0aad2c-eb76-447f-9549-03f909c3f109" alt="Banner" width="500" height="250">
        <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/09eedc2c-eb60-4f6f-9170-3fc8acc34e74" alt="Banner" width="500" height="250">
    </div>
</div>


<a name="arch"></a>
## 📝 Project Architecture
<div align="center">
  <img src="https://github.com/ZaidBenmr/Cryptocurrency-Data-Engineering-Project/assets/105943885/86090751-cc2c-4e54-aa5a-20f628e308e0" alt="Banner">
</div>

### 🛠️ Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Angular](https://img.shields.io/badge/angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

<a name="webscraping"></a>
## 🕸️ Web Scraping
I refined the web scraper by integrating Selenium to execute JavaScript code on the Yahoo Finance website, enhancing its capability to handle dynamic content. Each coin now has a dedicated scraping job that pushes data into its respective Kafka topic. Subsequently, a Python listener job consumes this data, performs necessary data quality checks and transformations, and finally stores it in a MongoDB collection.
The main challenge for this scraping task is that the job needs to scroll down the website before parsing data to load the on-demand loading data.

<a name="installation"></a>
## 🖥️ Installation : 
Clone the repository:

```
git clone https://github.com/BENAMAR-Zaid/Cryptocurrency-Analytics-ETL.git
```

### - Configure Kafka Streaming Broker (Windows)

1. Start ZooKeeper & Kafka server:

```
zookeeper-server-start.bat .\config\zookeeper.properties
kafka-server-start.bat .\config\server.properties

```

2. Create the necessary Kafka topic and configure the rentention time :

First create for each coin a topic to produce the historical data : 
```
kafka-topics.bat --create --topic coinname-raw --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

For each coin create a topic to produce snapshots of the day : 
```
kafka-topics.bat --create --topic topic-name --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-configs.bat --bootstrap-server localhost:9092 --entity-type topics --entity-name topic-name --alter --add-config retention.ms=30000
```

### - Configure MongoDB

1. Create a mongodb database : 

```
use cryptocurrencies
db.createCollection("dummyCollection")
db.dummyCollection.insert({dummyKey: "dummyValue"})
```

2. For each coin create a collection : 

```
db.createCollection("coinname_cleaned")
```

### - Run listeners

For each coin run the following listener

```
python "Historical data listener.py" --topicName "topic-name" --collectionName "coll-name"
```

### - Configure Logstash / Elasticsearch


1. for each coin create a index in elasticsearch :

```
curl -X PUT "localhost:9200/coinname_cleaned" -H "Content-Type: application/json"
```

2. Open Logstash transformation pipeline :

First you should configure pipeline file located on ``` config\pipelines.yml ```

Then run the following : 
```
bin\logstash
```

### - Run Django REST Framework APIs

1. Activate the virtual environnement :
   
```
Scripts\activate
```

2. Navigate to Cryptocurrency-djangoserver source file and run the server

```
cd src
```
```
python manage.py runserver
```

### - Run Angular Dashboard

Navigate to Angular Dashboard source file and run the project

```
cd src
```
```
ng serve
```

### - Airflow Orchestration 

After configuring the project components you can now run the Airflow environnement and run the following dag : 

Scheduling scraping jobs to run daily :

```
scrape_last_histdata_dag.py
```

### - Open Power BI dashboard 

#### Now that the project is successfully running, the data jobs will daily scrape the latest historical data for each coin and push it into the ETL data pipeline.

<a name="contact"></a>
## 📨 Contact Me

[LinkedIn](https://www.linkedin.com/in/zaid-benamar/) •
[Gmail](zaid.benmr@gmail.com)

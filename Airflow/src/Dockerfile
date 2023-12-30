FROM apache/airflow:latest

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    chromium  && \
    apt-get autoremove -yqq --purge && \
    apt-get clean

USER airflow

# Install Python packages required by your scripts
RUN pip install pandas \
                bs4 \ 
                selenium \
                confluent-kafka \
                pymongo \
                webdriver-manager==3.5.3
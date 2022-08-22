FROM python:3.9.1

RUN pip install pandas pytrends google-cloud-bigquery

WORKDIR /app

COPY collect_trends.py helper_functions.py ./

ENTRYPOINT [ "python", "collect_trends.py"]
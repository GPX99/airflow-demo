# Apache Airflow

To use `statsd_datadog_enabled`, require to install the datadog package

Docker Build Airflow custom image with the following command:
```
docker build -f infra/docker/apache-airflow/Dockerfile -t <name>:<tag> .
```

Once you generated the new image, please replace `<name>:<tag>` in demo-values and restart the airflow service.

# google_trends

This is a simple script which pulls data from Google trends and saves them as a BigQuery table. For exercise purposes, the script has been dockerized.

## Example usage

Build Docker image

```bash
docker build -t google_trends:v001
```

Export LOCAL_PATH variable:
```bash
export LOCAL_PATH=path_to_folder_with_your_credentials
```

Run Docker container (example):

```bash
  docker run -it \
  --volume=${LOCAL_PATH}/.google_cred.json:/secrets/key.json \
  --env=GOOGLE_APPLICATION_CREDENTIALS=/secrets/key.json \
    google_trends:v001 \
      --keyword=mealkits \
      --start_date=2022-01-01 \
      --end_date=2022-01-15 \
      --project=google-cloud-project \
      --dataset=big-query-dataset
```


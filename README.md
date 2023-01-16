# fastapi-datastore

A FastAPI DataStore example


Using datastore emulatore to test

https://cloud.google.com/datastore/docs/tools/datastore-emulator

```bash
virtualenv .venv
source .venv/bin/activate

pip install -r requirements.txt 

gcloud beta emulators datastore start --no-store-on-disk

$(gcloud beta emulators datastore env-init)

uvicorn main:app --reload
```
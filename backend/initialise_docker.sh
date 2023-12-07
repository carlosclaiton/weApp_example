#!bin/bash
docker stop fastapi_server
docker rm fastapi_server
docker build -t fastapi .
docker run --name fastapi_server -p 8000:8000 -d fastapi
#!bin/bash
docker stop webapp_db
docker rm webapp_db
docker build -t web_postgress_db .
docker run --name webapp_db -e POSTGRES_PASSWORD=test123 -e POSTGRES_USER=myuser -p 5432:5432 -d   web_postgress_db
git checkout main  ## Docker image for a postgres database

After clone the repo into your local folder, navigate to the folder and run
 
```bash
docker build -t <image_name> .
```

to start the app container, you can choose a password and user and the name of the container
 
```bash
docker run --name <container_name> -e POSTGRES_PASSWORD=test123 -e POSTGRES_USER=myuser -p 5432:5432 -d  <image_name>
```
 
Check if it is up running using
 
```bash
docker ps
```
 
you should have somehting like
 
```bash
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
5be8cdff5c96   <image_name>   "docker-entrypoint.s…"   19 seconds ago   Up 19 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   <container_name>
```
 
To stop the container you then run
 
```bash
docker stop <container_name>
```
 
to connect to the database through terminal you then can connect inside the docker container by running the following command:
 
```bash
docker exec -it <container_name> bash
```
now we can stablish connection with the Database
 
```bash
psql -U myuser
```
to check the existing database you can use

```bash
\l
```
you can then connect to the newlly created database 

```bash
\c webapp_db
```

and you can check the content of the table  

```bash
select * from clients
```
from the migration files you should have the following return

 client_id | firstname |  surname  |       email       |         created_on         
-----------+-----------+-----------+-------------------+----------------------------
         1 | Maria     | Valentina | maria.v@gmail.com | 2023-12-05 06:23:43.959704
(1 row)

Congratulations you have your PostgreSQL database running on your Docker container

# using lastest version of postgres
FROM postgres

#copy schema
COPY ./migrations/ /docker-entrypoint-initdb.d/

#expose the port application
EXPOSE 5432

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# put herr the connection string to your database
DATABASE_URL_ind = "postgresql://myuser:test123@localhost:5432/webapp_db"

# using here the name of the service from the dockercompose file for the service 
# DATABASE_URL = "postgresql://myuser:test123@db:5432/webapp_db"

# Getting the connection string from the enviroment passed though docker file
DATABASE_URL = os.environ.get("DATABASE_URL", DATABASE_URL_ind)

# define the engine using the url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)
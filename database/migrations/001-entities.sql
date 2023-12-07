-- connect to the database
\c webapp_db

CREATE TABLE clients (
	client_id serial PRIMARY KEY NOT NULL,
	firstname VARCHAR ( 50 ) NOT NULL,
	surname VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL DEFAULT NOW()
    -- last_login TIMESTAMP 
);

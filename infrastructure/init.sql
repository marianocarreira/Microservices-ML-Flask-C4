-- Drop databases if they exist
DROP DATABASE IF EXISTS "logging-db";
DROP DATABASE IF EXISTS "users-db";

-- Create the "users-db" database
CREATE DATABASE "users-db";
\c "users-db";

-- Create the "user" table
CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    apiKey TEXT NOT NULL,
    suscriptionName TEXT NOT NULL,
    suscriptionRpm INTEGER NOT NULL
);

-- Switch back to the default database (assumed to be "postgres")
\c "postgres";

-- Create the "logging-db" database
CREATE DATABASE "logging-db";
\c "logging-db";

-- Create the "log_entry" table
CREATE TABLE log_entry (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    "dataType" INTEGER NOT NULL,
    "data" TEXT NOT NULL
);
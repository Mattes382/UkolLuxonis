-- Connect to the default database (postgres)
\c postgres;

-- Create the database if it doesn't exist
SELECT 'CREATE DATABASE sreality' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'sreality');

-- Connect to the newly created database
\c sreality;

-- Create the scraped_data table if it doesn't exist
CREATE TABLE IF NOT EXISTS scraped_data (
    id SERIAL PRIMARY KEY,
    title TEXT,
    image_url TEXT
);

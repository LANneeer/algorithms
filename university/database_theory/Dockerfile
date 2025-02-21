FROM postgres:latest

# Environment variables for PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=postgres

# Copy the SQL file to docker-entrypoint-initdb.d to run it on container start
COPY ./init.sql /docker-entrypoint-initdb.d/

# Use official PostgreSQL as base (choose your version, e.g., 16)
FROM postgres:16

# Install pgvector extension
RUN apt-get update && \
    apt-get install -y postgresql-16-pgvector && \
    rm -rf /var/lib/apt/lists/*

# Expose default Postgres port
EXPOSE 5432

# Set default environment variables (override with -e in docker run if needed)
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=db

ETL Project for LAS to pgpointcloud
This project implements an ETL pipeline to extract LAS files from an S3 bucket, process them using a PDAL pipeline, and load the results into a PostgreSQL database with the pgpointcloud extension. The pipeline runs in Docker for portability and reproducibility.
Setup
(To be updated with installation and usage instructions)
Requirements

Python 3.9+
Docker and docker-compose
AWS credentials for S3 access
PostgreSQL 14+ with pgpointcloud extension

Project Structure

src/: Source code for the ETL pipeline
extract/: Code for pulling LAS files from S3
transform/: Code and json filea for PDAL pipeline processing and loading to pgpointcloud
main.py: Main script to run the ETL


config/: Configuration files (e.g., config.yaml)
tests/: Unit tests for the pipeline
Dockerfile: Docker configuration for the ETL
docker-compose.yml: Docker Compose setup for PDAL library, PostgreSQL and ETL
.env:

#!/bin/bash

# Check if docker-compose is installed
if ! command -v docker-compose &> /dev/null
then
    echo "Error: docker-compose is not installed. Please install it before running this script."
    exit 1
fi

# Run docker-compose up
docker-compose up -d
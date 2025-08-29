#!/bin/bash

# Script to run the Box Office API in Docker

echo "🚀 Starting Box Office API with Docker..."

# Create data directory if it doesn't exist
mkdir -p data

# Build and run the container
docker-compose up --build

echo "✅ Container started! API available at http://localhost:8000"
echo "📖 API Documentation: http://localhost:8000/docs"
echo "🛑 To stop: docker-compose down"

#!/bin/bash

# Build images
docker-compose up --build -d

# sleep function
echo "Sleep 5 seconds to wait for all tests to finish"
sleep 5
docker-compose logs --no-color >& api_test.log

# Cleanup
docker-compose down

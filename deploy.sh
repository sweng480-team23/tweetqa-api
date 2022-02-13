#!/usr/bin/env bash

# Deploy to Cloud Run
# gcloud builds submit

# To run the docker instance locally, uncomment below...
docker build -t tweetqa-api .
docker run -p 8080:8080 tweetqa-api

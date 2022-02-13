#!/usr/bin/env bash

# Deploy to Cloud Run
gcloud builds submit

# To run the docker instance locally, uncomment below...
# docker run -p 8080:8080 tweetqa-api

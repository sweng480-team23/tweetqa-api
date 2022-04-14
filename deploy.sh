#!/usr/bin/env bash

# Deploy to Cloud Run
 gcloud builds submit

# To clear local system docker cache objects
#docker system prune --all --force

# To run the docker instance locally, uncomment below...
#docker build -t tweetqa-api .
#docker run -p 8080:8080 tweetqa-api

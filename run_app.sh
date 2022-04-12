echo "SECRET_KEY=$1" >> .env
echo "RUNNER_ADDRESS=$2" >> .env
echo "SENDGRID_API_KEY=$3" >> .env
gunicorn --timeout 300 -b :8080 main:app
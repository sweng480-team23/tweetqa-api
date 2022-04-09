echo "SECRET_KEY=$1" >> .env
echo "RUNNER_ADDRESS=$2" >> .env
echo "GMAIL_PWD=$3" >> .env
gunicorn --timeout 300 -b :8080 main:app
echo "SECRET_KEY=$1" >> .env
echo "RUNNER_IP=$2" >> .env
echo "GMAIL_PWD=$3" >> .env
gunicorn -b :8080 main:app
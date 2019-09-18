echo "Restarting the docker services"

# Shut down the docker
docker-compose down;
docker-compose rm;

docker-compose up -d;
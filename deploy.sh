# Build the UI
echo "Building React"
cd react && npm i && npm run build && cd ..

echo "Restarting the docker services"

# Shut down the docker
docker-compose down;
docker-compose rm;

# Remove the old image
docker rmi -f server_flask

docker-compose up -d;
# Build conda image
if echo "docker ps -a | grep -q conda-imagecl"
then
  echo "Conda image already exists";
else
  echo "Creating conda image..."
  cd conda || exit;
  docker build -t conda-imagecl .
  cd .. || exit;
fi

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
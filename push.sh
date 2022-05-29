. ./build.sh

echo "Pushing Docker images -> $IMAGE_LABEL_VERSION and $IMAGE_LABEL_LATEST ...."
docker push $IMAGE_LABEL_VERSION
docker push $IMAGE_LABEL_LATEST
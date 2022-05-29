sh package.sh
IMAGE_LABEL_LATEST='jpsalamarcara/joe_services:latest'
IMAGE_LABEL_VERSION='jpsalamarcara/joe_services:dev'
docker build -t ${IMAGE_LABEL_LATEST} -t ${IMAGE_LABEL_VERSION} -f docker/service.Dockerfile .

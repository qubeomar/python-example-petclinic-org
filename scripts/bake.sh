#!/bin/bash
set -o allexport

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/..

IMAGE_NAME=pypet
IMAGE_VERSION=latest

docker build -t $IMAGE_NAME:$IMAGE_VERSION .


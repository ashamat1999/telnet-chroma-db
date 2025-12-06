# Agent to production

Para pruebas locales, se puede usar adk api_server

## Export Requirements
poetry export -f requirements.txt --output requirements.txt --without-hashes

## Get Fast API app
from google.adk.cli.fast_api import get_fast_api_app

## Create Dockerfile
### Run dockerfile
docker build . -t rag-agent
docker run rag-agent

### Stop containers
docker container ls
docker rm -f <name>

# Dockerfile

# pull the official docker image
FROM python:3.11.1-slim AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock /project/
COPY . project/

WORKDIR /project

RUN pdm install
RUN pdm run download_model

EXPOSE 8080
CMD ["pdm", "run", "start"]
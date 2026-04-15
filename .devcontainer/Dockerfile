FROM mcr.microsoft.com/devcontainers/python:3-3.11-trixie

RUN apt-get update && apt-get install -y pyenv && \
    pip install --upgrade pip && \
    pip install pipenv

ADD Pipfile  Pipfile.lock /

RUN pipenv install --system --deploy --dev
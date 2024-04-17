FROM mcr.microsoft.com/devcontainers/python:3.12

RUN apt-get update && apt-get install -y ffmpeg mp3val flac xdg-utils vim less

USER vscode

RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 -

WORKDIR /app
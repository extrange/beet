FROM python:3-bullseye

RUN apt-get update && apt-get install -y ffmpeg mp3val flac xdg-utils vim

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
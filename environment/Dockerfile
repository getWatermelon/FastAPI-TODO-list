FROM python:3.9.6-buster

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app
EXPOSE 8000

RUN pip install poetry==1.1.7

COPY ../pyproject.toml /app/pyproject.toml

RUN poetry config virtualenvs.create false \
  && poetry install

RUN poetry install

COPY .. /app

CMD poetry run uvicorn app:app --host 0.0.0.0 --reload --log-level debug

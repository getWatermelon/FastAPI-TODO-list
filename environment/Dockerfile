FROM python:3.9.6-buster

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app
EXPOSE 8000

RUN pip install poetry

COPY ../pyproject.toml /app/pyproject.toml
COPY ../poetry.lock /app/poetry.lock

RUN poetry config virtualenvs.create false \
  && poetry install

COPY .. /app

#CMD poetry run uvicorn app.main:app --host 0.0.0.0 --reload --log-level debug
CMD poetry run python app/main.py

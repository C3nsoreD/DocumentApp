FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Document_verifier

COPY requirements.txt /Document_verifier/

RUN pip install -r requirements.txt

COPY . /Document_verifier/

FROM python:3.9@sha256:0208c1b66de6e22480b3ad6334fc4fe2ef030572cf1fb1f699e68038fafcad00

RUN pip install --upgrade pip

WORKDIR /app

COPY ./support/requirements.txt ./support/
RUN pip install --no-cache-dir --requirement ./support/requirements.txt

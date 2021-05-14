FROM python:3.6-buster

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY checkpoint checkpoint
COPY makerpage makerpage

ENV FLASK_APP=makerpage
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=7000

CMD [ "flask", "run", "--host=127.0.0.1" ]
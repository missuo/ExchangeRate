FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

ENV FLASK_APP=card-org.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["gunicorn", "card-org:app"]

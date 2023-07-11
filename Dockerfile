FROM python:3.9-slim-buster

WORKDIR /Speech_cleaner

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 5000

# HEALTHCHECK CMD curl --fail http://localhost:5000/

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
 
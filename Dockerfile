FROM python:3.9-slim-buster

WORKDIR /Speech_cleaner

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000
# EXPOSE 5000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
 

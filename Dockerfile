FROM python:latest

RUN pip install flask

COPY . .

CMD ["python", "/vlunapp/app.py"]
FROM python:3.6.8

RUN pip install flask

COPY . .

CMD ["python", "/vlunapp/app.py"]
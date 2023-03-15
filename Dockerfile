FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ADD MyFirstFlask.py MyFirstFlask.py

CMD ["python", "MyFirstFlask.py"]


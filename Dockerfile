FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

VOLUME /app/data

COPY . .

CMD ["python", "./tests/python.py"]

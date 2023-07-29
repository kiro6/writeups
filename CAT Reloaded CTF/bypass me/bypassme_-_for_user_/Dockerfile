FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get upgrade -y
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mv flag.txt /


EXPOSE 7080


CMD ["python", "app.py"]

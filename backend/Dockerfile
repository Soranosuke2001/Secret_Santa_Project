FROM python:3.12

LABEL maintainer = "sschlegel1@my.bcit.ca"

RUN apt-get update && apt-get install -y sqlite3

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD python main.py

FROM python:3.12

LABEL maintainer = "sschlegel1@my.bcit.ca"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD python reset_data.py && python main.py

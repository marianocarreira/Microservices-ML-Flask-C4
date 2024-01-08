FROM python:3.11.2-alpine3.17

WORKDIR /logging-ms

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

COPY . .
COPY entrypoint.sh entrypoint.sh

RUN chmod u+x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000
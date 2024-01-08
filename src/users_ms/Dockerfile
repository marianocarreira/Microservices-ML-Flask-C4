FROM python:3.11.2-alpine3.17

WORKDIR /users_ms

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.sh entrypoint.sh

COPY . .

RUN chmod u+x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8020
FROM python:3.11.2-alpine3.17

WORKDIR /api_gateway

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py"]

EXPOSE 8080
FROM python:3.9
WORKDIR /predictions_ms

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

EXPOSE 8010
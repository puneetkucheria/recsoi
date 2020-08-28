FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python", "./run.py" ]

CMD exec guicorn --bind :$PORT --workers 1 --threads 8 app:run

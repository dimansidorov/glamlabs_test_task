FROM python:3.11.0-alpine

WORKDIR /src

RUN apk update && apk add gcc libc-dev
RUN pip install --upgrade pip

COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY . /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

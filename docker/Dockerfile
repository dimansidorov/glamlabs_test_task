FROM joyzoursky/python-chromedriver

WORKDIR /src

RUN pip install --upgrade pip

COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY . /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

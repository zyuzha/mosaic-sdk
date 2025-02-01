FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirement.txt

CMD ["python3", "-m", "examples.simple_connection"]
FROM python:3.10.0-alpine3.14

COPY dns_checker.py dns_file.txt requirements.txt /

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3","/dns_checker.py"]

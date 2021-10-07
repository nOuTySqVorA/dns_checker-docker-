FROM ubuntu

COPY dns_checker.py /
COPY dns_file.txt /
COPY requirements.txt /

RUN apt update && apt upgrade -y && apt install python3 python3-pip -y && pip3 install -r requirements.txt

ENTRYPOINT ["python3","/dns_checker.py"]

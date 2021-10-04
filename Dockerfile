FROM ubuntu

RUN apt update && apt upgrade && apt install dnsutils -y

COPY dns_checker /
COPY dns_file.txt /

ENTRYPOINT ["/dns_checker"]

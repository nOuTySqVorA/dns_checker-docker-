FROM ubuntu

RUN apt update && apt upgrade && apt install dnsutils -y

COPY dns_checker /

ENTRYPOINT ["/dns_checker"]

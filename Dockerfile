FROM ubuntu

RUN apt update && apt upgrade && apt install dnsutils -y && apt install whois && apt install -y --no-install-recommends ntp

COPY dns_checker /
COPY dns_file.txt /

ENTRYPOINT ["/dns_checker"]

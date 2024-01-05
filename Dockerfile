FROM ubuntu:20.04

RUN apt-get update && apt-get install -y wget curl sudo docker.io net-tools

RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

CMD ["bash"]

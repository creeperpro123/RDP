FROM ubuntu:20.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y wget curl sudo docker.io net-tools && \
    curl -fsSL https://github.com/docker/compose/releases/download/1.29.2/docker-compose-Linux-x86_64 -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

RUN echo "alias docker-compose='docker-compose'" >> ~/.bashrc

RUN apt-get install -y xterm && \
    echo "xterm" > ~/.bashrc

CMD ["xterm"]

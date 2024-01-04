FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    curl \
    sudo \
    wget

RUN echo 'root:17021983' | chpasswd

RUN apt-get update && apt-get install -y systemd

RUN systemctl daemon-reload

ENTRYPOINT ["systemd", "&&", "/bin/bash"]

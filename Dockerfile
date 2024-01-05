FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    neofetch \
    net-tools \
    curl

RUN echo 'root:17021983' | chpasswd

CMD ["/bin/bash"]

FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y systemd && \
    rm -rf /var/lib/apt/lists/* && \
    systemctl mask \
        tmp.mount \
        etc-hostname.mount \
        etc-hosts.mount \
        etc-resolv.conf.mount \
        display-manager.service \
        getty.target \
        graphical.target \
        kmod-static-nodes.service \
        systemd-logind.service \
        systemd-remount-fs.service \
        systemd-update-utmp.service && \
    systemctl set-default multi-user.target
VOLUME [ "/sys/fs/cgroup" ]

CMD ["/lib/systemd/systemd"]

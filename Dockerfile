FROM fredblgr/ubuntu-novnc:20.04
 
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  systemd systemd-sysv dbus dbus-user-session
EXPOSE 80
 
# Set the environment variable for screen resolution
ENV RESOLUTION 1707x1067
 
# Start the command to run NoVNC
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

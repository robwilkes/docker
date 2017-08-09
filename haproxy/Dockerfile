#HAProxy
FROM haproxy:1.7
COPY etc/haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
RUN mkdir -p /run/haproxy && touch /run/haproxy/admin.sock
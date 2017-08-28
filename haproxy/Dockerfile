#HAProxy
FROM haproxy:1.7
COPY etc/haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
RUN mkdir -p /run/haproxy && \
    touch /run/haproxy/admin.sock && \
    apt-get update && \
    apt-get install -y openssl ca-certificates

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
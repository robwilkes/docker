#HAProxy
FROM haproxy:1.7
COPY etc/haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY docker-entrypoint.sh /
RUN mkdir -p /run/haproxy && \
    touch /run/haproxy/admin.sock && \
    chmod +x /docker-entrypoint.sh
    apt-get update && \
    apt-get install -y openssl ca-certificates

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
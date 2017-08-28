#!/bin/sh
set -e

if [ ! -f /usr/local/etc/haproxy/ssl/private/selfsigned.pem ]; then
    echo "Self Signed Certificate not found"
    echo "Generating Self Signed Certificate"
    mkdir -p /usr/local/etc/haproxy/ssl/private
    openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /usr/local/etc/haproxy/ssl/private/selfsigned.key -out /usr/local/etc/haproxy/ssl/private/selfsigned.crt -subj "/C=AU/ST=NSW/L=Sydney/O=Docker/OU=Test/CN=localhost"
    cat /usr/local/etc/haproxy/ssl/private/selfsigned.crt /usr/local/etc/haproxy/ssl/private/selfsigned.key > /usr/local/etc/haproxy/ssl/private/selfsigned.pem
    chmod -R 600 /usr/local/etc/haproxy/ssl/private
    echo "Generating Self Signed Certificate... Done"
fi

# first arg is `-f` or `--some-option`
if [ "${1#-}" != "$1" ]; then
	set -- haproxy "$@"
fi

if [ "$1" = 'haproxy' ]; then
	# if the user wants "haproxy", let's use "haproxy-systemd-wrapper" instead so we can have proper reloadability implemented by upstream
	shift # "haproxy"
	set -- "$(which haproxy-systemd-wrapper)" -p /run/haproxy.pid "$@"
fi

exec "$@"
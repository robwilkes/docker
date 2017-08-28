#!/bin/sh
set -e

if [ ! -f /usr/local/etc/exabgp/exabgp.env ]; then
    echo "exabgp.env not found, generating with defaults"
    /usr/local/sbin/exabgp --fi > /usr/local/etc/exabgp/exabgp.env
    echo "exabgp.env not found, generating with defaults... done"
fi

exec "$@"
# Dockerized HAProxy #

## Description ##
HAProxy within Docker.

Sample configuration provided, which copied to:
/usr/local/etc/haproxy/haproxy.cfg

Added a few extra packages (openssl), now generates a self signed certificate on boot.
(since I hate having anything unencrypted, even if it's a demo)

Binds stats socket to *:1936
Binds sample frontend to *:443

This is an example only, the intention is to map this to a local path on the host, combined with ExaBGP to annouce a loopback VIP.

## Run ##
With built in sample config:
```
docker run \
    --network=host \
    --cap-add=NET_ADMIN \
    --restart=unless-stopped \
    -p 443:443 \
    -p 1936:1936 \
    -d \
    --name haproxy \
    robwilkes/haproxy
```

With config on docker host:
```
docker run \
    --network=host \
    --cap-add=NET_ADMIN \
    --restart=unless-stopped \
    -p 443:443 \
    -p 1936:1936 \
    -d \
    -v /usr/local/etc/haproxy:/usr/local/etc/haproxy
    --name haproxy \
    robwilkes/haproxy
```

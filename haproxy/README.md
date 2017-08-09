# Dockerized HAProxy #

## Description ##
HAProxy within Docker.

Sample configuration provided, which copied to:
/usr/local/haproxy/etc/haproxy.cfg

Binds stats socket to *:1936
Binds sample frontend to *:80

This is an example only, the intention is to map this to a local path on the host, combined with ExaBGP to annouce a loopback VIP.

## Run ##
With built in sample config:
```
docker run \
    --network=host \
    --cap-add=NET_ADMIN \
    -p 80:80 \
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
    -p 80:80 \
    -p 1936:1936 \
    -d \
    -v /usr/local/haproxy/etc:/usr/local/haproxy/etc
    --name haproxy \
    robwilkes/haproxy
```

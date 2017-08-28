# Dockerized ExaBGP #

## Description ##
ExaBGP within Docker.

Sample configuration provided, which copied to:
/usr/local/etc/exabgp/exabgp.cfg

Binds new loopback address: 1.1.1.1/32
Looks for haproxy process (pid) and if it exists, announces the loopback address to upstream device.

This is an example only, the intention is to map this to a local path on the host, running whatever configuration you want, running only the application within the container.

## Run ##
With built in sample config:
```
docker run \
    --network=host \
    --cap-add=NET_ADMIN \
    -p 179:179 \
    -d \
    --name exabgp \
    robwilkes/exabgp
```

With config on docker host:
```
docker run \
    --network=host \
    --cap-add=NET_ADMIN \
    -p 179:179 \
    -d \
    -v /usr/local/etc/exabgp:/usr/local/etc/exabgp
    --name exabgp \
    robwilkes/exabgp
```

## LOGS ##

exabgp will log to stdout, so ```docker logs -f exabgp``` will let you view them.
# Dockerized ExaBGP #

## Description ##
ExaBGP within Docker.

Sample configuration provided, which is copied to:
/usr/local/etc/exabgp/exabgp.cfg

Binds new loopback address on host: 1.1.1.1/32
Checks if localhost is listening on port 443, if it is announces 1.1.1.1/32 to upstream router.

This is an example only, the intention is to map local volume on host with your desired configuration, running only the application within the container.

## Run ##
With built in sample config:
```
docker run \
    --network=host \
    --cap-add=NET_ADMIN \
    --restart=unless-stopped \
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
    --restart=unless-stopped \
    -p 179:179 \
    -d \
    -v /usr/local/etc/exabgp:/usr/local/etc/exabgp
    --name exabgp \
    robwilkes/exabgp
```

## LOGS ##

exabgp will log to stdout, so ```docker logs -f exabgp``` will let you view them.
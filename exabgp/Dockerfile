#ExaBGP
FROM debian:jessie-backports
RUN apt-get update \
        && apt-get install -qy \
                wget \
                python

WORKDIR /root
ENV EXABGP_VERSION 3.4.20
ENV exabgp.daemon.user=root

COPY docker-entrypoint.sh /

RUN wget -O exabgp.tar.gz "https://github.com/Exa-Networks/exabgp/archive/${EXABGP_VERSION}.tar.gz" \
        && mkdir exabgp \
        && tar -xzf exabgp.tar.gz -C exabgp --strip-components=1 \
        && cp -R exabgp/lib/exabgp /usr/lib/python2.7/dist-packages \
        && cp exabgp/bin/* /usr/local/bin \
        && cp exabgp/sbin/* /usr/local/sbin \
        && mkdir -p /usr/local/etc/exabgp \
        && mkdir -p /usr/local/bin/exabgp \
        && chmod +x /docker-entrypoint.sh

RUN wget "https://raw.githubusercontent.com/robwilkes/ipaddr-py/master/ipaddr.py" \
	&& cp ipaddr.py /usr/local/lib/python2.7/dist-packages/

ADD bin /usr/local/bin/exabgp/
COPY etc/exabgp.cfg /usr/local/etc/exabgp/exabgp.cfg

EXPOSE 179

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/local/sbin/exabgp","/usr/local/etc/exabgp/exabgp.cfg"]
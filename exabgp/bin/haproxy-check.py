#!/usr/bin/env python
import sys
from haproxystats import HAProxyServer

URL = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]
MODE = sys.argv[4]
VERIFY = False if sys.argv[5].lower() == 'verify_false' else True
COMP = sys.argv[6]
NAME = sys.argv[7]

haproxy = HAProxyServer(URL,USER,PASS,MODE,VERIFY)

if COMP == 'backend':
    for b in haproxy.backends:
        if b.name == NAME and b.status == 'UP':
            print('%s: %s' % (b.name, b.status))
            sys.exit(0)
elif COMP == 'frontend':
    for b in haproxy.frontends:
        if b.name == NAME and b.status == 'OPEN':
            print('%s: %s' % (b.name, b.status))
            sys.exit(0)

print('%s: %s' % (sys.argv[2], 'DOWN'))
sys.exit(1)
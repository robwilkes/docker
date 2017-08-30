#!/usr/bin/env python
import sys
from haproxystats import HAProxyServer

URL = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]
MODE = sys.argv[4]
BEND = sys.argv[5]
VERIFY = False if sys.argv[6].lower() == 'false' else True

haproxy = HAProxyServer(URL,USER,PASS,MODE,VERIFY)

for b in haproxy.backends:
    if b.name == BEND and b.status == 'UP':
        print('%s: %s' % (b.name, b.status))
        sys.exit(0)

print('%s: %s' % (sys.argv[2], 'DOWN'))
sys.exit(1)
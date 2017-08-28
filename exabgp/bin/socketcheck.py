#!/usr/bin/env python

import socket
import sys

def is_alive(address, port):
    """ This is a function that will test TCP connectivity of a given
    address and port. If a domain name is passed in instead of an address,
    the socket.connect() method will resolve.

    address (str): An IP address or FQDN of a host
    port (int): TCP destination port to use

    returns (bool): True if alive, False if not
    """

    # Create a socket object to connect with
    s = socket.socket()

    # Now try connecting, passing in a tuple with address & port
    try:
        s.connect((address, port))
        return True
    except socket.error:
        return False
    finally:
        s.close()

if is_alive(sys.argv[1], int(sys.argv[2])):
    sys.exit(0)
else:
    sys.exit(1)
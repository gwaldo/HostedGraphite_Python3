#! /usr/bin/env python3

import socket

conn = socket.create_connection(("carbon.hostedgraphite.com", 2003))
conn.send("YOUR-API-KEY.foo 1.2\n".encode('utf-8'))
conn.close()
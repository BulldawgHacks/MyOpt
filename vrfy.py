#!/usr/bin/env python3

import socket
import sys

if len(sys.argv) != 3:
    print("Usage: vrfy.py <username_file> <ip_address>")
    sys.exit(0)

# Read the list of usernames
with open(sys.argv[1], 'r') as f:
    usernames = f.read().splitlines()

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect = s.connect((sys.argv[2], 25))

# Receive the banner
banner = s.recv(1024)

print(banner.decode())

# VRFY each user
for user in usernames:
    s.send(('VRFY ' + user + '\r\n').encode())
    result = s.recv(1024)
    print(result.decode())

# Close the socket
s.close()

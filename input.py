import logging
import asyncio
import sys

from kademlia.network import Server

import communication.py

while 1:
    message = input(">>> ")
    communication.send(0000.0000.0000.0000, 8468, sys.argv[1] + sys.argv[2], message)

import logging
import asyncio
import sys
import time

from kademlia.network import Server

import communication.py

while 1:
    message = input(">>> ")
    communication.get(0.0, 8468, sys.argv[1] + sys.argv[2])
    time.sleep(5)
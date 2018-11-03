import logging
import asyncio
import sys


from kademlia.network import Server


def get(node, port, key):
    # print("Usage: python get.py <bootstrap node/ip> <bootstrap port/port> <key/siehe server-node>")

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log = logging.getLogger('kademlia')
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    server = Server()
    server.listen(8469)
    bootstrap_node = (str(node), port}
    loop.run_until_complete(server.bootstrap([bootstrap_node]))
    result = loop.run_until_complete(server.get(key))
    server.stop()
    loop.close()

    print("Get result:", result)

def send(node, port, key, value):

    # print("Usage: python get.py <bootstrap node/ip> <bootstrap port/port> <key/siehe server-node> <value>")
  
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log = logging.getLogger('kademlia')
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    server = Server()
    server.listen(8469)
    bootstrap_node = (str(node), int(port))
    loop.run_until_complete(server.bootstrap([bootstrap_node]))
    loop.run_until_complete(server.set(key, value))
    server.stop()
    loop.close()

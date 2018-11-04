import logging
import asyncio
import sys
import datetime

from kademlia.network import Server



def send( port, key, message):
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
    bootstrap_node = ("0.0.0.0", int(port))
    loop.run_until_complete(server.bootstrap([bootstrap_node]))
    result = loop.run_until_complete(server.get(key))

    loop.run_until_complete(server.set(key, str(result) + str(datetime.datetime.now()) + "  " + message))
    result = loop.run_until_complete(server.get(key))
   
    server.stop()
    #loop.close()

    print("************************************************")
    print(key , "\n" , result + "\n")
    print("************************************************")



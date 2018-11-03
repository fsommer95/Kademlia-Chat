import asyncio
from kademlia.network import Server
import sys

if len(sys.argv) != 2:
    print("Usage: python connect.py <Username>")
    print(len(sys.argv))
    sys.exit(1)

# Create a node and start listening on port 5678
node = Server()
node.listen(5678)

loop = asyncio.get_event_loop()
loop.run_until_complete(node.bootstrap([("0000.0000.0000.0000", 8468)]))

#create a List with Users, stored at the first_node

#if empty, create one
if loop.run_until_complete(node.get("Users")) == None:
 loop.run_until_complete(node.set("Users", "") )

    
loop.run_until_complete(node.set("Users", loop.run_until_complete(node.get("Users")) + "  " + sys.argv[1]))

# get the value associated with "my-key" from the network
result = loop.run_until_complete(node.get("Users"))
print(result)

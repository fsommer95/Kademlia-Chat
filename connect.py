import asyncio
from kademlia.network import Server
import sys
import os


#print the List of Users
def list_of_users():
    users = loop.run_until_complete(node.get("Users"))
    return users
   

def name_request():
    print ("what is your name?")
    global name
    name = input(">>> ")
    

def extend_users():
    #create a List with Users, stored at the first_node
    #if empty, create one
    if loop.run_until_complete(node.get("Users")) == None:
        loop.run_until_complete(node.set("Users", " "))

    loop.run_until_complete(node.set("Users", loop.run_until_complete(node.get("Users")) + "  " + name))
    list_of_users()

def check_mate(mate):
    if mate in list_of_users():
        return True
    else:
        return False

# Create a node and start listening on port 5678
node = Server()
node.listen(5678)

loop = asyncio.get_event_loop()

#localhost
loop.run_until_complete(node.bootstrap([("0.0.0.0", 8468)]))

name_request()

if name == "":
    print("please enter a name")
    name_request()
       
extend_users()

while 1:
    print("chat starts")

    print ("who wuld you like to chat with?")    
    list_of_users()
    print (list_of_users())

    mate = input(">>> ")

    if check_mate(mate):
        print ("You chose" + mate) 

        #open new termainal for chat
        os.system("python3 input.py " + name + " " + mate)
        os.system("python3 overview.py " +  name + " " +  mate)

    else:
        print("not a user")



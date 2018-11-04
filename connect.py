import asyncio
from kademlia.network import Server
import sys
import os
import send



#print the List of Chats
def list_of_Chats():  
    Chats = loop.run_until_complete(node.get("Chats"))
    return Chats
   
# get the Users Name
def name_request():
    print ("what is your name?")
    global name
    name = input(">>> ")
       
#check if the chat is existent
def check_mate(mate):
    if mate in list_of_Chats():
        return True
    else:
        return False

def readChat(chatname):
    Chats = loop.run_until_complete(node.get(chatname))
    print(Chats)


def writeChat(chatname, message):
    #create a List with Chats, stored at the first_node
    #if empty, create one
    if loop.run_until_complete(node.get(chatname)) == None:
        loop.run_until_complete(node.set(chatname, " "))

    loop.run_until_complete(node.set(chatname, loop.run_until_complete(node.get(chatname)) + name + ":  " + message + "\n"))
    list_of_Chats()


def createnewChat(chatname):
    #create a List with Chats, stored at the first_node
    #if empty, create one
    if loop.run_until_complete(node.get(chatname)) == None:
        loop.run_until_complete(node.set(chatname, " "))

    loop.run_until_complete(node.set("Chats", loop.run_until_complete(node.get("Chats")) + chatname +  "\n"))
    readChat(chatname)
   
#add a new chat
def extend_Chats(chatname):
    #create a List with Chats, stored at the first_node
    #if empty, create one
    if loop.run_until_complete(node.get("Chats")) == None:
        loop.run_until_complete(node.set("Chats", " "))

    loop.run_until_complete(node.set("Chats", loop.run_until_complete(node.get("Chats")) + "  " + chatname))
    list_of_Chats()
    

# Create a node and start listening on port 5678
node = Server()
node.listen(5678)

loop = asyncio.get_event_loop()

#localhost
loop.run_until_complete(node.bootstrap([("0.0.0.0", 8468)]))

name_request()




while 1:

    print("The existing chats are: ")
    print(list_of_Chats())

    print("Would you like to kreate a new chat? (Yes = y; No = n )")
    newChat = input(">>> ")
        
    if newChat == "y":
        print("What is the name of the new chat?")
        chat = input(">>> ")

        #print("Extend chats")
        #extend_Chats(chat)
        
        print("Createnewchat")
        extend_Chats(chat)


        #print("write first entry")
        #write = input(name + ": >>> ")
        #writeChat(chat, write)
        #print("send") 
        #send.send( 8468, chat, "" )
        #get.read(8468, chat)

        #print("read1")
        #readChat(chat)
        #get.read(8468, chat)


    print("which chat would you like to join? \n")

    print("List of Chats:")
    print(list_of_Chats())

    chat = input(">>> ")

    if check_mate(chat):
        print ("You chose chat: " + chat) 

        while 1:    
            write = input(name + ": >>> ")


            print("write2")
            send.send( 8468, chat, name + ":  " +  write + "\n")
            #send.send( 8468, chat, write )
            #get.read(8468, chat)
            #writeChat(chat, write)
            #readChat(chat)
            #get.read(8468, chat)
            

    else:
        print("not a chat")











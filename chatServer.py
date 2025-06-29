from socket import *
from test_chatDB2 import chatDB
from threading import Thread
import threading
from time import ctime

class clientHandler(Thread):
    def __init__(self,client,record,address):
        Thread.__init__(self)
        self._client = client
        self._record = record
        self._address = address

    def broadcastMessage(self,activeClient,message):
        for socket in CONNECTIONS_LIST:
            if socket != server and socket != activeClient:
                try:
                    msg = str.encode(message)
                    socket.send(msg)
                except:
                    print("Client (%s) is proably offline" %self._address)

                    broadcastMessage(socket,("Client (%s) is proably offline" %self._address))

                    socket.close()
                    CONNECTIONS_LIST.remove(socket)


    def run(self):
        self._client.send(str.encode("Welcom to the chat room!!"))
        self._name = bytes.decode(self._client.recv(BUFSIZE))

        allMessage = self._record.getmsg(0)
        self._client.send(str.encode(allMessage))
        while True:
            message = bytes.decode(self._client.recv(BUFSIZE))
            if message == "quit":
                print('Client disconnected')
                self._client.close()
                CONNECTIONS_LIST.remove(self._client)
                break
            else:
                message = ctime() + ': ['+ self._name +'] --> ' + message
                self._record.insertmsg(message)
                threadLock.acquire()
                self.broadcastMessage(self._client,message)
                threadLock.release()




HOST = '10.34.1.50'
PORT = 5000
BUFSIZE = 4096
ADDRESS = (HOST,PORT)
CONNECTIONS_LIST = []
threadLock = threading.Lock()
record = chatDB()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
MAX_CLIENT = 10
server.listen(MAX_CLIENT)
CONNECTIONS_LIST.append(server)
print("Chat server has started on port: ", str(PORT))

while True:
    print("Waiting for connection...")
    client, address = server.accept()
    print("...connected from: ",address)
    threadLock.acquire()
    CONNECTIONS_LIST.append(client)
    threadLock.release()
    handler = clientHandler(client,record,address)
    handler.start()

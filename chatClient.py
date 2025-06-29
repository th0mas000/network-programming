from socket import *

HOST = '10.34.1.50'
PORT = 5000
BUFSIZE = 4096
ADDRESS = (HOST,PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
msgfromserver = bytes.decode(server.recv(BUFSIZE))
print(msgfromserver)
name = input('Enter your name: ')
userName = str.encode(name)
server.send(userName)

while True:
    receiveMessage = bytes.decode(server.recv(BUFSIZE))
    if not receiveMessage:
        print('Srever disconnected')
        break
    print(receiveMessage)
    sendMessage = input(':>> ')
    if not sendMessage:
        print('Server disconnected')
        break
    server.send(str.encode(sendMessage))

server.close()
    
        

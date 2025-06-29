import socket

IP_SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_SERVER, PORT))
#client.sendall(bytes("This is from client", 'UTF-8'))

while True:
    #data = client.recv(2048)
    #print("From server:", data.decode())
    to_server = input("To server>>")
    code = to_server.strip()
    if code == "01":
        tmp = "1#" + code + "#12345"
    elif code == "02":
        tmp = "1#" + code + "#CPU info"
    elif code == "03":
         tmp = "1#" + code + "#MEM info"
    elif code == "99":
         tmp = "1#" + code + "#Disconnect"
    else:
        print("Your code is not supprt!!")
    client.sendall(bytes(tmp, 'UTF-8'))
    msg_from_server = client.recv(2048)
    msg = msg_from_server.decode()
    tmp = msg.strip()
    proto = tmp.split('#')
    ver = proto[0]
    code = proto[1]
    cinfo = proto[2]
    
    if to_server == "99":
        break
    if code == "04":
        print("Authentication OK")
    elif code == "05":
        print("Authentication Fail")
    elif code == "06":
        print("CPU is ", cinfo, "%")
    elif code == "07":
        print("Memory is ", cinfo, "MB")
    elif code == "98":
        print("unknown!!")
    else:
        print("snmp protocol is not support!")
client.close()

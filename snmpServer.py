import socket, threading
import psutil
import os

class client(threading.Thread):
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        print("New connection from client:", clientAddress)

    def run(self):
        print("Connecion from:", clientAddress)
        msg = ""
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            #authentication msg
            tmp = msg.strip()
            proto = tmp.split('#')
            ver = proto[0]
            code = proto[1]
            cinfo = proto[2]
            print("from client >>", msg)
            if code == "99":
                break
            elif code == "01":
                if cinfo == "12345":
                    tmp = "1#04#OK"
                    self.csocket.send(bytes(tmp, 'UTF-8'))
                else:
                    tmp = "1#05#NO"
                    self.csocket.send(bytes(tmp, 'UTF-8'))
            elif code == "02": #cpu
                load1, load5, load15 = psutil.getloadavg()
                cpu_usage = (load15/os.cpu_count()) * 100
                tmp = "1#06#" + str(cpu_usage)
                self.csocket.send(bytes(tmp, 'UTF-8'))
            elif code == "03": #mem
                mem = psutil.virtual_memory().percent
                tmp = "1#07#" + str(mem)
                self.csocket.send(bytes(tmp, 'UTF-8'))
            else:
                tmp = "1#98#unknown your code"
                self.csocket.send(bytes(tmp, 'UTF-8'))
            #self.csocket.send(bytes(msg, 'UTF-8'))
        print("Client of ",clientAddress, " disconnected!")

IP = '127.0.0.1'
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
print("SNMP Server started already..")
print("Wating for SNMP client request..")
while True:
    s.listen(5)
    clientSock, clientAddress = s.accept()
    snmpClient = client(clientAddress, clientSock)
    snmpClient.start()

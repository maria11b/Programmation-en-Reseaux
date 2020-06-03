from socket import *
from threading import *

clients = set()

def clientThread(clientSocket, clientAddress):
    while True:
        message = clientSocket.recv(1024).decode("utf-8")
        print(clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message)
        for client in clients:
            if client is not clientSocket:
                client.send((clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message).encode("utf-8"))

        if not message:
            clients.remove(clientSocket)
            print(clientAddress[0] + ":" + str(clientAddress[1]) +" disconnected")
            break

    clientSocket.close()

hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

hostIp = "192.168.100.5"
portNumber = 8080
hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
print ("Asteptam conectarea...")


while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.add(clientSocket)
    print ("Conexiune stabilita cu: ", clientAddress[0] + ":" + str(clientAddress[1]))
    thread = Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()
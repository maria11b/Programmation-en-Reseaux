from socket import *
from threading import *
from tkinter import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "192.168.100.5"
portNumber = 8080

clientSocket.connect((hostIp, portNumber))

window = Tk()
window.title("Conectat la: "+ hostIp+ ":"+str(portNumber))

txtMessages = Text(window, width=50)
txtMessages.grid(row=0, column=0, padx=10, pady=10)

txtYourMessage = Entry(window, width=50)
txtYourMessage.insert(0,"Mesajul tau")
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

def sendMessage():
    clientMessage = txtYourMessage.get()
    txtMessages.insert(END, "\n" + "You: "+ clientMessage)
    clientSocket.send(clientMessage.encode("utf-8"))

btnSendMessage = Button(window, text="Send", width=20, command=sendMessage)
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

def recvMessage():
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        txtMessages.insert(END, "\n"+serverMessage)

recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

window.mainloop()


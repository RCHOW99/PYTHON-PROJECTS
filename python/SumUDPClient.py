from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
isrunning = True
isint = True

while isrunning:
    message = (input("Enter any number of integers:(eg 1 2 3 4)\nOr type \"exit\" to exit\n"))
    if message == "exit":
        isrunning = False
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
        clientSocket.close()
    if message != "exit":
        try:
            x = list(map(int, message.split()))
            isint = True
        except:
            isint = False
        if isint:
            clientSocket.sendto(message.encode(), (serverName, serverPort))
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print(modifiedMessage.decode())
    if isint == False and isrunning == True:
        print("<WARNING> No numbers are entered!\n")

# Implementation Based On Code From
# Computer Networking. A Top-Down Approach (2021)
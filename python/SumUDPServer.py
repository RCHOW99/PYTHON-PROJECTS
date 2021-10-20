from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
isrunning = True
while isrunning:
    print("The server is ready to receive......")
    message, clientAddress = serverSocket.recvfrom(2048)

    if message.decode() == "exit":
        isrunning = False
        modifiedMessage = "Client Closed"
        print("Server Closed")
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        serverSocket.close()

    elif message.decode() != "exit":
        x = list(map(int, message.split()))
        SumNum = sum(x)
        AvgNum = round(sum(x) / len(x), 2)
        MaxNum = max(x)
        MinNum = min(x)
        Sum = "Sum = " + str(SumNum) + "\n"
        Avg = "Average = " + str(AvgNum) + "\n"
        Max = "Max = " + str(MaxNum) + "\n"
        Min = "Min = " + str(MinNum) + "\n"
        modifiedMessage = Sum + Avg + Max + Min
        print(modifiedMessage)
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

# Implementation Based On Code From
# Computer Networking. A Top-Down Approach (2021)
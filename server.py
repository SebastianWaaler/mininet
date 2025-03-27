#import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
serverSocket.bind(('127.0.0.1', 8000))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            continue

        filename = message.split()[1]
        f = open(filename[1:], 'rb')
        outputdata = f.read()
        f.close()

        # Send one HTTP header line into socket
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length: " + str(len(outputdata)) + "\r\n"
        response_header += "Content-Type: text/html\r\n\r\n"
        connectionSocket.sendall(response_header.encode())

        # Send the content of the requested file to the client
        connectionSocket.sendall(outputdata)
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        response = "HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
        connectionSocket.sendall(response.encode())

        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data


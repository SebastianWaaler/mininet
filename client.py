import socket
import argparse

# Function to create a simple HTTP client to send GET requests to the server
def http_client(server_ip, server_port, filename):
    # Format the HTTP GET request
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}\r\nConnection: close\r\n\r\n"

    # Create a TCP socket to connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, server_port))  # Connect to the server
        client_socket.sendall(request.encode('utf-8'))  # Send the GET request

        response = b""  # Initialize a variable to store the response
        while True:
            chunk = client_socket.recv(1024)  # Receive data in chunks
            if not chunk:  # If there's no more data, exit the loop
                break
            response += chunk  # Append the received chunk to the response

    # Print the server response
    print("Server Response:")
    print(response.decode('utf-8', errors='ignore'))  # Print the response (ignore decoding errors)

# Command line interface for the client using argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple HTTP Client")
    parser.add_argument("-i", required=True, help="Server IP address")
    parser.add_argument("-p", type=int, required=True, help="Server port number")
    parser.add_argument("-f", required=True, help="Filename to request")

    args = parser.parse_args()  # Parse command line arguments
    http_client(args.i, args.p, args.f)  # Call the function with the parsed arguments

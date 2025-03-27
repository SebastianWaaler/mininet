import socket
import sys
import argparse

# Function to send an HTTP GET request to the server
def http_client(server_ip, server_port, filename):
    try:
        # Create a socket and establish a TCP connection with the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        # Construct the HTTP GET request
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}\r\nConnection: close\r\n\r\n"

        # Send the request to the server
        client_socket.sendall(request.encode())

        # Receive and store the server response
        response = b""
        while True:
            part = client_socket.recv(1024)  # Receive data in chunks of 1024 bytes
            if not part:
                break  # Exit loop if no more data is received
            response += part

        # Decode and print the server response
        print(response.decode())

        # Close the connection to the server
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")

# Main execution block
if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Simple HTTP Client")
    parser.add_argument("-i", "--ip", required=True, help="Server IP Address")
    parser.add_argument("-p", "--port", type=int, required=True, help="Server Port")
    parser.add_argument("-f", "--file", required=True, help="Filename to request")

    # Parse arguments provided by the user
    args = parser.parse_args()

    # Call the HTTP client function with parsed arguments
    http_client(args.ip, args.port, args.file)

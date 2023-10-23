import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Server is listening for connections...")

    client_socket, client_address = server_socket.accept()

    print(f"Connection established with {client_address}")

    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

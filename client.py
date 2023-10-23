import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    message = "test"
    client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()

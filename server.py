import socket
import threading


#the adi cipher
def cc(data):
    data = [ord(i)+1 for i in data]
    final=''
    for i in data:
        final+=chr(i)

    return final


def dd(data):
    data = [ord(i)-1 for i in data]
    final=''
    for i in data:
        final+=chr(i)

    return final

def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode()
        dec=dd(message)
        if not dec:
            print(f"Connection to {client_address} closed")
            break

        # Print received message
        print(f"Client ({client_address}): without cipher {message}")

        print(f"Client ({client_address}): {dec}")

        # Send message back to client
        response = input("Server: ")
        enc=cc(response)
        client_socket.send(enc.encode())

        if dec == 'bye':
            client_socket.close()
            break
        if response == 'bye':
            client_socket.close()
            return

    # Close client connection
    client_socket.close()

def main():
    host = ''
    port = 12345

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    # Accept incoming client connections
    client_socket, client_address = server_socket.accept()
    # Handle client connection in a separate thread
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

if __name__ == "__main__":
    main()
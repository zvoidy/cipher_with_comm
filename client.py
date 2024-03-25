import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
def encrypt(data):
    data = [ord(i) + 1 for i in data]
    final=''
    for i in data:
        final+=chr(i)
    return final
sock.connect(server_address)

def decrypt(data):
    data = [ord(i) - 1 for i in data]
    final=''
    for i in data:
        final+=chr(i)
    return final

while True:
    message = input("Enter data to send : ")
    print(f'sending {message}')
    if message=="bye":
        sock.close()
        break
    data = encrypt(message)
    sock.sendall(data.encode('utf-8'))
    data = sock.recv(1024).decode()
    print(f'received :{decrypt(data)}') 
    if decrypt(data) == 'bye':
        sock.close()
        break
    
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 3443))
server_socket.listen(1)

while True:
    (client_socket, addr) = server_socket.accept()
    msg = client_socket.recv(1024)
    print(str(msg, "utf8"))
   
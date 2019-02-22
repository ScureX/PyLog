import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = (('127.0.0.1', 3443))
client_socket.connect(server_addr)
client_socket.send(bytes("yeet", "utf8"))
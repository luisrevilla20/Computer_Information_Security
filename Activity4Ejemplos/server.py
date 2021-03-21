import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1337))
s.listen(1)
connection, address = s.accept()
with connection:
    data = connection.recv(1024)
    print(data.decode("ascii"))
    connection.close()
s.close()

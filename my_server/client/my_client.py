import socket

sock = socket.socket()
sock.connect(('172.17.0.1', 9999))

while True:
    str_data = str(input('\n>'))
    if str_data == 'close':
        break
    sock.send(str_data.encode())
    data = sock.recv(1024)
    print(data.decode('utf-8'), end='', flush=True)
    if not data:
        break

sock.close()

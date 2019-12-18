import socket

def my_server(sock):
    sock.bind(('0.0.0.0', 9999))
    sock.listen(1)
    print('I work')
    while True:
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            str_data = data.decode('utf-8')
            if not data:
                break
            print(str_data, flush=True)
            conn.send(data)
            if str_data == 'close server':
                print("Server was closed by client", flush=True)
                conn.close()
                return
        conn.close()


sock = socket.socket()
my_server(sock)
sock.close()

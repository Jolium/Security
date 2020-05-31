import socket


class Server:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def serve(self):
        hostport = (self.host, self.port)
        self.socket.bind(hostport)
        self.socket.listen(1)
        # results = self.socket.accept()
        # print('\n'.join(map(str, results)))
        conn, addr = self.socket.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if data:
                    print(data)
        # self.socket.close()


if __name__ == '__main__':
    server = Server('localhost', 8081)

    server.serve()

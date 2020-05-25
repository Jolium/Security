import socket


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return f'Scanner: {self.ip}'

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lower_port, upper_port):
        for port in range(lower_port, upper_port + 1):
            if self.is_open(port):
                self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0
        
    def write(self, file_path):
        open_port = map(str, self.open_ports)
        with open(file_path, 'w') as f:
            f.write('\n'.join(open_port))


def main():
    ip = '192.168.56.104'
    scanner = Scanner(ip)
    scanner.scan(1, 65000)
    print(scanner.open_ports)
    scanner.write('./open_ports.txt')


if __name__ == '__main__':
    main()

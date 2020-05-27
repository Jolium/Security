from port_scanner import Scanner
from grabber import Grabber
import settings
from utils import time_func


def main():
    ip = settings.IP_ADDRESS
    scanner = Scanner(ip)
    scanner.scan(settings.START_PORT, settings.END_PORT)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(f'{port}: {grabber.read()}')
            grabber.close()
        except Exception as e:
            print('Error', e)


if __name__ == '__main__':
    main()

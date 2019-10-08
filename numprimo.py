# -*- coding: utf-8 -*-

def run():

    number = int(raw_input('Introduzca un número: '))
    prime = is_prime(number)

    if prime:
        print('{} es un número primo'.format(number))
    else:
        print('{} no es un número primo'.format(number))

def is_prime(number):
    # result = True
    if number == 0:
        return False
    if number < 0:
        number = -1 * number
    if number < 4:
        return True
    else:
        for i in range (2, number):
            if number % i == 0:
                # print ('Es divisible entre {}: {}'.format(i, result))
                return False
    return True

if __name__ == "__main__":
  run()

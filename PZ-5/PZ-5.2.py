#Описать функцию InvertDigits(K), меняющую порядок следования цифр целого положительного
# числа К на обратный (К - параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой
# функции поменять порядок следования цифр на обратный для каждого из пяти данных целых чисел.
import random


def InvertDigits(K):
    s = str(K['K'])
    s_new = s[::-1]
    K['K'] = int(s_new)


R = {'K': None}
for i in range(5):
    R['K'] = random.randrange(1, 10000)
    print("Число ", i + 1, ": ", R['K'])
    InvertDigits(R)
    print('Измененное = ', R['K'])
    print()
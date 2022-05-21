#!/usr/bin/python3
import random


def isGood():
    print('isGood')
    return True


def isBad():
    print('isBad')
    return False


if __name__ == '__main__':
    if isBad() and isGood():
        print("Hello")
    else:
        print("World")

    random_list = []
    for i in range(0, 100):
        n = random.randint(1, 1000000)
        random_list.append(n)
    print(random_list)

    # shuffle_random_list = [908900, 178205, 547076, 708523, 416143, 789551, 508511, 20072, 641569, 211679, 501221, 992895, 897642, 3143, 697747, 304335, 200869, 114172, 410068, 584747, 766003, 765686, 69330, 742957, 506422, 247447, 512372, 345052, 961457, 87811, 49724, 205719, 494496, 735125, 965328, 675978, 727027, 176478, 48253, 47948, 558749, 210635, 7887, 943116, 352829, 488068, 740071, 794296, 945365, 883162]
    # random.shuffle(shuffle_random_list)
    # print(shuffle_random_list)

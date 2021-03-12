import string
import random
import hashlib
import threading
from threading import Thread
from hashlib import sha256
import time
import sys


switch = 0


def pass_gen():
    f = open('pass.txt', 'w')
    letters = string.ascii_lowercase
    temp = len(letters)
    for i in range(temp):
        for j in range(temp):
            for k in range(temp):
                for l in range(temp):
                    for m in range(temp):
                        passwd = ""
                        passwd = str(letters[i]) + str(letters[j]) + str(letters[k]) + str(letters[l]) + str(letters[m])
                        f.write(passwd + '\n')

    f.close()



def Hash(x, hash, n, x_1, *pass_arr):
    start_time = time.time()
    j = 1
    if x_1 >= 11881376:
        x_1 = 11881376

    for i in range(x, x_1):
        #print('1')
        if j == 1:
            #print('razmer massiva   '+ str(len(pass_arr))+ '\n')
            print("Запускаем поток " + str(n + 1) + " с позиции " + str(x) + '('+str(pass_arr[i])+')' + '\n')
            #print(line)
            #print(x, x_1, '\n')
            j = 2
        m = sha256(pass_arr[i].encode('utf-8')).hexdigest().rstrip()

        if m == hash:
            print('Хеш подобран в потоке номер ' + str(n+1) + '\n')
            print('Выбраный хеш: ' +str(hash))
            print("Пароль: " + str(pass_arr[i]))
            print("--- %s seconds ---" % (time.time() - start_time))




def hash_gen():
    f = open('hash_d.txt', 'w')
    f_p = open('pass.txt', 'r')
    for line in f_p:
        f.write(sha256(line.rstrip().encode('ascii')).hexdigest() + '\n')



def main():
    # pass_gen()
    # hash_gen()
    pass_arr = []
    with open('pass.txt') as f:
        line_pass = sum(1 for _ in f)
    with open('pass.txt') as f:
        for line in f:
            pass_arr.append(line.rstrip())

    f_h = open('hash.txt', 'r')

    i = 1
    for line in f_h:
        print(str(i) + str('. ') + line)
        i += 1
    f_h.close()
    print("Введите номер хеша")
    hash_no = input()
    print("Введите колличество потоков")
    threads_num = int(input())

    x = line_pass / threads_num

    with open('hash.txt', 'r') as f_h:
        for i in range(int(hash_no) - 1):
            f_h.readline()
        hash = f_h.readline().rstrip()

    for i in range(int(threads_num)):
        a = int(i * x)
        x1 = int(a+(i+1 * x))
        th = Thread(target=Hash, args=(a, hash, i, x1, *pass_arr))
        th.start()

if __name__ == '__main__':
   main()







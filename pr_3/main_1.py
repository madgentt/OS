from multiprocessing import Process, Queue, Value
import time
import sys
import os

switch_w = Value('d', 0)
switch_t = Value('d', 0)
q = Queue()

def work(q):
    #print("worker start")
    while(1):
        time.sleep(0.1)
        q.put([1])
        if switch_w.value == 3:
            return
        if q.qsize() >= 100 or switch_w.value == 1:
            #print("workers stop")
            switch_w.value = 1
            return


def take(q):
    #print("taker start")
    while(1):
        time.sleep(0.1)
        q.get()
        if q.qsize() == 0 or switch_t.value == 1:
            #print("taker stop")
            switch_t.value = 1
            return
        #print("take")

def run():
    takers = []
    workers = []

    for i in range(200):
        q.put([1])

    for i in range(3):
        worker = Process(target=work, args=(q,))
        workers.append(worker)
        worker.start()
    for i in range(2):
        taker = Process(target=take, args=(q,))
        takers.append(taker)
        taker.start()

    while 1:
        time.sleep(1)
        #print(q.qsize())
        #print("switch = "+ str(switch.value))

        if switch_w.value == 3:
            for i in workers:
                #print("kill")
                #print(i.is_alive)
                i.kill()
            switch_w.value = 4
            break

        if switch_w.value == 1.0 : #Если больше 100 эллементов
            for i in workers:
                #print("kill")
                #print(i.is_alive)
                i.kill()
            switch_w.value = 2

        if q.qsize() <= 80 : #Если эллементов стало меньше 80
            switch_w.value = 0
            workers = []
            #print("start again")
            for i in range(3):
                worker = Process(target=work, args=(q,))
                worker.start()
                workers.append(worker)

        if switch_t.value == 1:
            for i in takers:
                i.kill
            switch_t.value = 2

        if q.qsize() > 0 and switch_t.value == 2:
            switch_t.value =0
            workers = []
            for i in range(3):
                taker = Process(target=take, args=(q,))
                takers.append(taker)
                taker.start()



def stop(runer):
    switch_w.value = 3
    #print('11111111111111111111111111')
    while 1:
        if q.qsize() == 0:
            print("\nКОнвеер остановлен\n")
            runer.kill()
        return



def main():
    menu_switch = '0'
    while 1:

        if menu_switch == '0':
            print("\nВыберите что хотите сделать\n1.Запустить конвеер\n2.Состояние конвеера\n3.Выход\n")
        if menu_switch == '1':
            print("\nВыберите что хотите сделать\n1.Остановить конвеер\n2.Состояние конвеера\n3.Выход\n")

        switch = input()
        if switch == '1' and menu_switch == '0':
            runer = Process(target=run, args=())
            runer.start()
            switch = 0
            menu_switch = '1'
            print('a')
        if switch == '1' and menu_switch == '1':
            stoper = Process(target=stop, args=(runer,), daemon=True)
            stoper.start()
            switch = 0




        if switch == '2':
            os.system('clear')
            print("Чисел в очереди: " + str(q.qsize()))

            switch = '0'
        if switch == '3':
            if menu_switch == '1':
                runer.kill()
            sys.exit()


if __name__ == '__main__':
   main()

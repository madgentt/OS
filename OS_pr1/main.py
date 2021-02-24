import psutil
import os
import shutil
import json
import lxml.etree
import lxml.builder

def p_1():
    ### print(psutil.disk_partitions())
        for p in psutil.disk_partitions():
                print("Device: ", p.device)
                print("Mountpoint: ", p.mountpoint)
                print("FStype: ", p.fstype)


        total, used, free = shutil.disk_usage("/")
        print("Total: %d GiB" % (total // (2 ** 30)))
        print("Used: %d GiB" % (used // (2 ** 30)))
        print("Free: %d GiB" % (free // (2 ** 30)))
""""
    def case(switch):
        switcher = {
            1 : "1",
            2 : 2,
        }
        print switcher.get(switch, "Invalid month")
"""


def p_2():
    print("Выберете что хотите сделать:")
    print('1. Создать новый файл')
    print('2. Записать в файл')
    print('3. Вывести файл в консоль')
    print('4. Удалить файл')
    switch = input()
    if switch == '1':
        print("Введите путь к файлу")
        path = input()
        file = open(path, 'w+')
    if switch == '2':
        print("Введите путь к файлу")
        path = input()
        file = open(path, 'a')
        print("Введите текст")
        temp = input()
        file.write(temp)
    if switch == '3':
        print("Введите путь к файлу")
        path = input()
        file = open(path, 'r')
        temp = file.read()
        print(temp)
    if switch == '4':
        print("Введите путь к файлу")
        path = input()
        print("Вы уверены что хотите удалить файл? 1-Да, 2-Нет")
        x=input()
        if x == '1':
            os.remove(path)
        if x == '2':
            return


def p_3():
    print('Выберете что хотите сделать\n1.Записать новый файл\n2.Прочитать файл в консоль\n3.Удалить файл')
    switch = input()
    if switch == '1':
        print("Введите путь к файлу")
        path = input()

        data = {}
        data['people'] = []
        data['people'].append({
            'name': 'Scott',
            'sname': 'Sc',
        })
        data['people'].append({
            'name': 'Larry',
            'sname': 'Lr',
        })
        data['people'].append({
            'name': 'Tim',
            'sname': 'Ti',
        })
        print('Сколько людей добавить')
        temp = input()
        for i in range(int(temp)):
            print(str(i+1)+". Введите имя и фамилию")
            temp = input()
            temp = temp.split(' ')
            data['people'].append(dict(name=temp[0], sname=temp[1]))


        with open(path, 'w') as outfile:
            json.dump(data, outfile)

    if switch == '2':
        print("Введите путь к файлу")
        path = input()
        with open('path') as json_file:
            data = json.load(json_file)
            for p in data['people']:
                print('Name: ' + p['name'])
                print('Sname: ' + p['sname'])
                print('')

    if switch == '3':
        print("Введите путь к файлу")
        path = input()
        print("Вы уверены что хотите удалить файл? 1-Да, 2-Нет")
        x=input()
        if x == '1':
            os.remove(path)
        if x == '2':
            return


def p_4():
    print('Выберете что хотите сделать\n1.Записать новый файл\n2.Прочитать файл в консоль\n3.Удалить файл')
    switch = input()
    if switch == '1':
        E = lxml.builder.ElementMaker()
        ROOT = E.root
        DOC = E.doc
        FIELD1 = E.field1
        FIELD2 = E.field2

        the_doc = ROOT(
            DOC(
                FIELD1('some value1', name='blah'),
                FIELD2('some value2', name='asdfasd'),
            )
        )

        print(lxml.etree.tostring(the_doc, pretty_print=True))

    if switch == '2':
       print(1)

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Выберете пункт")
    switch = input()
    if switch == '1':
        p_1()
    if switch == '2':
        p_2()
    if switch == '3':
        p_3()
    if switch == '4':
        p_4()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

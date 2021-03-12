import psutil
import os
import shutil
import json
import lxml.etree
import lxml.builder
from lxml import etree
from zipfile import ZipFile

def p_1():
        print(psutil.disk_partitions())
        for p in psutil.disk_partitions():
                print("Device: ", p.device)
                print("Mountpoint: ", p.mountpoint)
                print("FStype: ", p.fstype)

        total, used, free = shutil.disk_usage("/")
        print("Total: %d GiB" % (total // (2 ** 30)))
        print("Used: %d GiB" % (used // (2 ** 30)))
        print("Free: %d GiB" % (free // (2 ** 30)))
        print(shutil.disk_usage('D:/'))

def p_2():
    while(1):
        print("Выберете что хотите сделать:")
        print('1. Создать новый файл')
        print('2. Записать в файл')
        print('3. Вывести файл в консоль')
        print('4. Удалить файл')
        print('5. Назад')
        switch = input()
        if switch == '1':
            print("Введите название файла(без расширения)");path = input()
            file = open(path+".txt", 'w+')
        if switch == '2':
            print("Введите название файла(без расширения)");path = input()
            file = open(path+".txt", 'a')
            print("Введите текст")
            temp = input()
            file.write(temp)
        if switch == '3':
            print("Введите название файла(без расширения)");path = input()
            file = open(path+".txt", 'r')
            temp = file.read()
            print(temp)
        if switch == '4':
            print("Введите название файла(без расширения)");path = input() + ".txt"
            print("Вы уверены что хотите удалить файл? 1-Да, 2-Нет")
            x=input()
            if x == '1':
                os.remove(path)
            if x == '2':
                return
        if switch == '5':
            return

def p_3():
    while(1):
        print('Выберете что хотите сделать\n1.Записать новый файл\n2.Прочитать файл в консоль\n3.Удалить файл\n4.Назад')
        switch = input()
        if switch == '1':
            print("Введите название файла(без расширения)")
            path = input()+".json"

            data = {}
            data['people'] = []
            """
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
            """
            print('Сколько людей добавить')
            temp = input()
            for i in range(int(temp)):
                print(str(i+1)+". Введите имя и фамилию(через пробел)")
                temp = input()
                temp = temp.split(' ')
                data['people'].append(dict(name=temp[0], sname=temp[1]))

            with open(path, 'w') as outfile:
                json.dump(data, outfile)

        if switch == '2':
            print("Введите название файла(без расширения)")
            path = input()+".json"
            with open(path) as json_file:
                data = json.load(json_file)
                """
                for p in data['people']:
                    print('Name: ' + p['name'])
                    print('Sname: ' + p['sname'])
                    print('')
                """

            # Pretty Printing JSON string back
            print(json.dumps(data, indent=4, sort_keys=True))

        if switch == '3':
            print("Введите название файла(без расширения)")
            path = input()+".json"
            print("Вы уверены что хотите удалить файл? 1-Да, 2-Нет")
            x=input()
            if x == '1':
                os.remove(path)
            if x == '2':
                return

        if switch == '4':
            return

def p_4():
    print('Выберете что хотите сделать\n1.Записать новый файл\n2.Прочитать файл в консоль\n3.Удалить файл')
    switch = input()
    if switch == '1':
        print("Введите название файла(без расширения)")
        path = input() + ".xml"
        root = etree.Element("root")
        aa = etree.Element("aaФ")
        bb = etree.SubElement(aa, "bb")
        aa.text = input("Введите текст в аа\n")
        bb.text = input("Введите текст в бб\n")
        root.append(aa)
        root.append(bb)
        tree = etree.ElementTree(root)
        tree.write(path)


    if switch == '2':
        print("Введите название файла(без расширения)")
        path = input() + ".xml"
        tree = etree.parse(path)

        print(etree.tostring(tree.getroot(), pretty_print=True))
    # Press the green button in the gutter to run the script.

    if switch == '3':
        print("Введите название файла(без расширения)");
        path = input() + ".xml  "
        print("Вы уверены что хотите удалить файл? 1-Да, 2-Нет")
        x = input()
        if x == '1':
            os.remove(path)
        if x == '2':
            return


def p_5():
    print('Выберете что хотите сделать\n1.Создать архив в форматер zip\n2.Добавить файл в архив\n3.Разархивировать файл и вывести данные о нем\n4.Удалить файл и архив')
    switch = input()
    if switch == '1':
        print("Введите название файла(без расширения)")
        path = input()
        zip = ZipFile(path+".zip", 'w')
        zip.close()
    if switch == '2':
        print("Введите название архива(без расширения)");
        path = input()
        zip = ZipFile(path + ".zip", 'w')
        print("Введите название файла(с расширением)");
        path = input()
        zip.write(path)
        zip.close()
    if switch == '3':
        print("Введите название архива(без расширения)");
        path = input()
        zip = ZipFile(path + ".zip", 'w')
        print("Введите название файла(с расширением)");
        path = input()
        zip.extract(path)
        zip.close()
        print("Размер файла:", os.stat(path).st_size)
    if switch == '4':
        print("Введите название архива(без расширения)");
        path = input() + ".zip"
        print("Вы уверены что хотите удалить файл? 1-Да, 2-Нет")
        x = input()
        if x == '1':
            os.remove(path)
        if x == '2':
            return



if __name__ == '__main__':
    while(1):
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
        if switch == '5':
            p_5()
        if switch == '6':
            for i in range(10):
                print(i);
                print(i);


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

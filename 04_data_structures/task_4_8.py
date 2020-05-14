# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = '192.168.3.1'


ip=ip.split('.')
one, two, three, four = ip
one=int(one)
two=int(two)
three=int(three)
four=int(four)
print("{:<10}{:<10}{:<10}{:<10}".format(one, two, three, four))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(one, two, three, four))
	

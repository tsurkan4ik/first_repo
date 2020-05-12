# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
                      

command1 = command1.split()                 #сделал из строки список строк и приравнял к ссылке command1                                
print(command1)                                                               
command1 = command1[-1].split(',')          '''обратился к последнему элементу(строке) в списке, с помощью метода сплит
                                               разбил его на список строк используя разделитель "," '''
print(command1)         

command2 = command2.split()                                                   
print(command2)                                                               
command2 = command2[-1].split(',')                                            
print(command2)                                                         

command1 = set(command1)                #преобразование списка строк в множество
command2 = set(command2)    

command12 = command1&command2                 #вывел пересечение множеств с помощью операции &                               
command12 = list(command12)                   #преобразование множества в список                               

print(sorted(command12))                         #сортировка списка и выведение как результат выполнения скрипта                            

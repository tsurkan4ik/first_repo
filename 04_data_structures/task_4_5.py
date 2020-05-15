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
                      

command1 = command1.split()          # разделил строку command1 на список строк методом .split                                        
print(command1)                                                               
command1 = command1[-1].split(',')   # разделил последний элемент списка command1 на список строк с разделителем запятая                                         
print(command1)         

command2 = command2.split()                                                   
print(command2)                                                               
command2 = command2[-1].split(',')                                            
print(command2)                                                         

command1 = set(command1)			#преобразовал список строк в множество
command2 = set(command2)

command12 = command1&command2       #сделал операцию пересечения множеств, которая оставила только совпадающие значения                                          
command12 = list(command12)         #преобразовал получившееся множество в список                                         

print(sorted(command12))            # отсортировал получившийся список                                         


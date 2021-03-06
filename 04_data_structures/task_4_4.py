# -*- coding: utf-8 -*-
'''
Задание 4.4

Список vlans это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]


In [11]: vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10] 
    ...:                                                                               

In [12]: vlans = sorted(list(set(vlans)))          '''для списка vlans применил множество (set) оно автоматически 
						      оставило только уникальные значения, далее применил к множеству список (list)
						      который переделал из множества опять список, и к списку применил функцию сортировки sorted
						      которая отсортировала полученный уникальный список'''
							

In [13]: print(vlans)                                                                  
[1, 2, 3, 4, 10, 20, 30, 100]

In [14]:  

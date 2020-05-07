# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'

spisok = nat.split()               #переделываем строку в список с разделителем пробел, и делаем ссылку "spisok"
spisok[-2] = 'GigabitEthernet0/1'  #меняем значение в списке -2(что соответствует FastEthernet0/1) в значение GigabitEthernet0/1
razd = ','                         #определяем разделитель
print(razd.join(spisok))           #к разделителю 'razd' применить метод перевода из списка в строку .join , в качестве аргумента в () передать список 'spisok'
 

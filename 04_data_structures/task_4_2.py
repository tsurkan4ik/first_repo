# -*- coding: utf-8 -*-
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
mac = mac.replace('AAAA:BBBB:CCCC', 'AAAA.BBBB.CCCC')    #с помощью метода replace строка преобразовывается из ':' в '.'
                    

# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.split()  
type_prot = 'OSPF'
ip = ospf_route [1] 
metric =  (ospf_route [2]).strip('[]') 
NH = (ospf_route[4]).strip(',') 
update = (ospf_route [5]).strip(',') 
interface = ospf_route [-1] 

template = '''
Protocol:		{}
Prefix:			{}
AD/Metric:		{}
Next-Hop:		{}
Last update:		{}
Outbound Interface:	{}
'''

print(template.format(type_prot, ip, metric, NH, update, interface))

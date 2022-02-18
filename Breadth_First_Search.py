# -*- coding: utf-8 -*-

"""
Breadth first search algoritm in python

Author: Luiz Augusto da Silva

"""

from collections import deque
import queue
from typing import Counter

#class for nodes
class node:
    def __init__(self,name,visit):
        self.name:str = name
        self.visit:bool = visit

#states declared as node
rs = node('Rio Grande do Sul',True)
sc = node('Santa Catarina',False)
pr = node('Paraná',False)
sp = node('São Paulo',False)
mg = node('Minas Gerais',False)
ms = node('Mato Grosso do Sul',False)
rj = node('Rio de Janeiro',False)
es = node('Espírito Santo',False)
go = node('Goiás',False)
df = node('Distrito Federal0',False)
mt = node('Mato Grosso',False)
ba = node('Bahia',False)
to = node('Tocantins',False)
se = node('Sergipe', False)
al = node('Alagoas',False)
pe = node('Pernanbuco',False)
pb = node('Paraíba',False)
rn = node('Rio Grande do Norte',False)
ce = node('Ceará',False)
ma = node('Maranhão',False)
pa = node('Pará',False)
ap = node('Amapá',False)
am = node('Amazonas',False)
rr = node('Roraima',False)
ac = node('Acre',False)
ro = node('Roraima',False)
pi = node('Piauí',False)

#adding nodes in a dictionary
fork = dict()

fork['rn']=[ce,rn]
fork['pb']=[ce,pe,rn]
fork['pe']=[pi,al,ce,pb]
fork['al']=[se,pe]
fork['se']=[ba,al]
fork['ce']=[pi,pe,pb,rn]
fork['pi']=[ma,ba,pe,ce]
fork['ma']=[pa,to,pi]
fork['ap']=[pa]
fork['pa']=[am,mt,to,ma,ap]
fork['rr']=[am,pa]
fork['am']=[ac,ro,rr,pa]
fork['ac']=[am]
fork['to']=[mt,go,ba,pa,ma]
fork['ba']=[go,mg,es,to,pi,pe,se]
fork['ro']=[mt,am]
fork['mt']=[ms,go,ro,am,pa,to]
fork['df']=[go]
fork['go']=[ms,mg,mt,df,to,ba]
fork['es']=[rj,mg,ba]
fork['mg']=[sp,rj,es,go,ba]
fork['rj']=[sp,mg,es]
fork['sp']=[pr,ms,mg,rj]
fork['ms']=[pr,sp,mt,go]
fork['pr']=[sc,ms,sp]
fork['sc']= [rs,pr]
fork['rs']= [sc]

#queuing dictionary objects
queue_ = deque()

for x in fork:
    ListI_ = fork[x]
    while len(ListI_)>0:
        queue_.append(ListI_.pop())

#Breadth first search function specific for this algorithm
def bfs(nodeF,queue:deque): 
    counter = 0                                                             
    while len(queue)>0:  
        nodeC = queue.pop()                             
        if nodeC.visit == False:  
            counter += 1
            nodeC.visit = True                                                        
            print(nodeC.name +' visited')                        
            if nodeC.name == nodeF.name:                 
                print('\nYou arrived at your destination.\n')
                break
            else:
                for y in range(len(queue_)):
                    if nodeC.name == queue_[y].name:
                        queue_[y].visit = True
                queue.appendleft(nodeC)
                
    print('\n',counter,' states visiteds.\n')

inp = input('Enter the acronym of the state you want to go to: ') 

bfs(eval(inp),queue_)
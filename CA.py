#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")

import random

rules=[0,1,1,0, 1,0,1,0]
generations=20
A=0
clsLen=40
zRate=0.4

def given(x,y,z) :
    return x*4+y*2+z

def show(lit,Len) :
    i=0
    while i<Len :
        if lit[i]==1 :
            print("*",end="")
        else :
            print(" ",end="")
        i+=1
    print()
    

cls=[A]*clsLen
i=0
while i<clsLen :
    b=0
    if random.random()>zRate :
        b=1
    cls[i]=b
    i+=1    
show(cls,clsLen)

gen=1
while gen<=generations :
    j=1
    clsTmp=[A]*clsLen
    while j<(clsLen-1) :
        left  =cls[j-1]
        mid   =cls[j]
        right =cls[j+1]
        
        pot=given(left,mid,right)        
        clsTmp[j]=rules[pot]
        
        j+=1  

    cls=clsTmp
    show(cls,clsLen)
    gen+=1

print("done")


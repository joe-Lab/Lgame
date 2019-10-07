#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")

cls=[5,7,2,6,1,9,3]
clsLen=7

def swap(x,y) :
    tmp=cls[x]
    cls[x]=cls[y]
    cls[y]=tmp

mW=0
for mW in range(clsLen) :
    posi=0
    minN=101
    oW=mW
    
    while oW<clsLen :
        if minN>cls[oW] :
            minN=cls[oW]
            posi=oW         
        oW+=1
        
    swap(mW,posi)           
    mW+=1

print(cls)   
print("done")


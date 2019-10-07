#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")

cls=[1,3,8,4,2,9,5]
clsLen=7

def swap(x,y):
    tmp=cls[x]
    cls[x]=cls[y]
    cls[y]=tmp

mW=0
for mW in range(clsLen) :
    oW=mW
    while oW>0 :
        if cls[oW]<cls[oW-1] :
            swap(oW,oW-1)
        oW-=1
    mW+=1
    
print(cls)
print("done")
 

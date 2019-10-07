#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")

A=0
cls=[6,5,8,2,4,1,6]
clsLen=7

maxNm=0
cp1=0
while cp1<clsLen :
    if cls[cp1]>=maxNm :
        maxNm=cls[cp1]
    cp1+=1
    
basket=[A]*(maxNm+1)

cp2=0
while cp2<clsLen :
    basket[cls[cp2]]+=1
    cp2+=1

bp=0   
while bp<(maxNm+1) :
    summ=basket[bp]
    while summ>0 :    
        print(bp,end=",")
        summ-=1
    bp+=1
    
print()
print("done")


import numpy as np
import math as mt


def feladat_1():
    n=int(input('n='))
    tomb=np.zeros(n, dtype='int')
    for i in range(n):
        tomb[i]=int(input('tomb[i]='))
    for j in range(n-2):
        if tomb[j]==tomb[j+1]:
            print(j, j+1)


def feladat_3():
    n=int(input())
    a=0
    t=np.zeros(n,dtype='int')
    for i in range(n):
        t[i]=int(input())
        a+=abs(t[i])
    return a/n


def feladat_4():
    n=int(input())
    a=0
    b=1
    c=0
    for i in range(n):
        x=int(input())
        if x>0:
            b*=x
        elif x<0:
            a+=x
            c+=1
    return b, a/c


def feladat_5():
    n=int(input())
    t=np.empty(n, dtype='int')
    x=1
    y=0
    for i in range(n):
        t[i]=int(input())
        if t[i]<7:
            x*=t[i]
        elif t[i]>10:
            y+=t[i]
    return x, y


def feladat_7():
    li=[]
    while True:
        a=int(input())
        if a!=0:
            li.append(a)
        else:
            break
    max=-mt.inf
    for i in range(len(li)-2):
        x=(li[i] + li[i + 1] + li[i + 2]) / 3
        if x>max:
            max=x
    return max


def feladat_10(n, k):
    t=np.array(n, dtype='int')
    a=0
    for i in range(n):
        for j in range(i):
            if t[i]%j==0:
                a+=1
        if a>k:
            return i
    return -1


def feladat_11(matrix,n,m):
    a=0
    b=0
    for j in range(m):
        for i in range(n):
            if matrix[i][j]==0:
                a+=1
            elif matrix[i][j]<0:
                b+=1
            if a*2<=b:
                print(j)
                break


def feladat_12(matrix,n,m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j]%(i+j)==0:
                print(matrix[i][j])


def feladat_13(matrix,n,m):
    min=mt.inf
    for j in range(m):
        for i in range(n):
            if min>matrix[i][j]:
                min=matrix[i][j]
            if i==n-1:
                matrix[i][j]-=min


def feladat_15(matrix, n):
    for i in range(n):
        for j in range(n):
            if i==j:
                if matrix[i][j]!=0:
                    return False
    return True



def hatos1(n, m):
    hatos=np.zeros((n,m))
    for i in range(0,n):
        for j in range(0,m):
            if i==0 or i==n//2 or i==n-1:
                hatos[i][j]=42
            else:
                hatos[i][j]=32
        hatos[i][0]=42
        if i>n//2:
            hatos[i][m-1]=42
    for i in range(0,n):
        for j in range(0,m):
            print(chr(int(hatos[i][j])), end='')
        print('\n')

def hatos2():
    esetek=int(input())
    t=np.zeros(2*esetek, dtype='int')
    for i in range(0, esetek*2, 2):
        sor=input()
        sor=sor.strip()
        sor=sor.split(' ')
        t[i]=int(sor[0])
        t[i+1]=int(sor[1])
    print(t)
    for i in range(0, 2*esetek, 2):
        print(hatos1(t[i], t[i+1]))
def main():

if __name__=="__main__":
    main()
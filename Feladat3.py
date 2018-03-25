import numpy as np


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
    print(feladat_5())
if __name__=="__main__":
    main()
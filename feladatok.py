import math as mt
def feladat1(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)


def feladat3(x):
    if -2<x and x<0:
        print(2*x)
    elif 0<=x and x<2:
        print(x*x)
    elif x>2:
        print(10)
    else:
        print('A függvény nem definiált ebben a pontban')

def feladat4(a,b,c):
    min=a
    max=a
    if min>b:
        min=b
    elif min>c:
        min=c
    if max<b:
        max=b
    elif max<c:
        max=c
    print(min,max)

def feladat5(a,b,c,d):
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

def feladat6(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        s = (a + b + c) / 2
        t = mt.sqrt(s * (s - a) * (s - b) * (s - c))
        r = mt.sqrt(((s - a) * (s - b) * (s - c)) / s)
        R = (a * b * c) / (4 * t)
        print("R=%.2f és r=%.2f" %(R,r))
    else:
        print("hiba")


def feladat7(khossz,kszélesség,dhossz):
    k=2*khossz+2*kszélesség
    if k<dhossz:
        print(dhossz-k, "drót marad meg")
    elif k>dhossz:
        print(k-dhossz, "drót szükséges még")


def feladat8(x,a,b,c,d):
    if x<5:
        f=(3*x-5)
    elif 5<=x and x<=10:
        f=(10)
    elif x>10:
        f=9*x+1
    if a+c>2*d and b>0:
        E=d-3*b
    elif a+c<2*d and b<0:
        E=d+3*b
    else:
        E=4
    print(f,E)


def feladat12(elertpontszam, maxpontszam):
    szazalek=(elertpontszam/maxpontszam)*100
    if szazalek>=60:
        print('sikeres')
    else:
        print('sikertelen')


def feladat13(érdemjegy):
    if érdemjegy==5:
        print("jeles")
    elif érdemjegy==4:
        print('jó')
    elif érdemjegy==3:
        print('közepes')
    elif érdemjegy==2:
        print('elégséges')
    elif érdemjegy==1:
        print('elégtelen')
    else:
        print('hiba')


def feladat14(honapszam):
    if honapszam==1:
        print('január')
    elif honapszam==2:
        print('február')
    elif honapszam==3:
        print('március')
    elif honapszam==4:
        print('április')
    elif honapszam==5:
        print('május')
    elif honapszam==6:
        print('június')
    elif honapszam==7:
        print('július')
    elif honapszam==8:
        print('augusztus')
    elif honapszam==9:
        print('szeptember')
    elif honapszam==10:
        print('október')
    elif honapszam==11:
        print('november')
    elif honapszam==12:
        print('december')
    else:
        print('hiba')

def feladat16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            print(a)
            break


def feladat17(n):
    masolat=n
    uj=0
    while n!=0:
        szj=n%10
        uj=uj*10+szj
        n=n//10
    print(uj==masolat)

def feladat19(n):
    prim=True
    if n==1:
        prim=False
    for i in range(2,int(mt.sqrt(n)+1)):
        if n%i==0:
            prim=False
            break
    return prim




def main():
if __name__=="__main__":
    main()
import math as mt
def feladat1(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)


def feladat2hosszú(a,b,c):
    if a<b and a<c:
        print(a,end=' ')
        if b<c:
            print(b,c,end=' ')
        else:
            print(c,b)
    elif b<a and b<c:
        print(b,end=' ')
        if a<c:
            print(a,c,end=' ')
        else:
            print(c,a, end=' ')
    else:
        print(c, end=' ')
        if a<b:
            print(a,b,end=' ')
        else:
            print(b,a,end=' ')


def feladat2(a,b,c):
    lista=[a,b,c]
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    print(str(lista).strip('[]'))


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

def feladat9(a,b,c):
    d=b*b-4*a*c
    if d>=0:
        x1=(-b-mt.sqrt(d))/(2 * a)
        x2=(-b+mt.sqrt(d))/(2 * a)
        print('x1=', x1)
        print('x2=', x2)
    else:
        print('Nincs megoldás.')



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


def feladat15(a,b):
    hányados=0
    while a>=b:
        hányados+=1
        a=a-b
    print(hányados)


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


def feladat18(a,b):
    x=a
    y=b
    p=0
    while x>0:
        if not x%2==0:
            p=p+y
            x-=1
        else:
            x=x/2
            y=y+y
    print(p)


def feladat19(n):
    prim=True
    if n==1:
        prim=False
    for i in range(2,int(mt.sqrt(n)+1)):
        if n%i==0:
            prim=False
            break
    return prim



def feladat20(n):
    a=0
    b=1
    c=a+b
    if n==1:
        print(a)
    elif n==2:
        print(a,b, end=' ')
    else:
        c=a+b
        print(a, b, c, end=' ')
        k = 3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c, end=' ')
            k+=1


def feladat21(n):
    if len(str(n))>9:
        print("Túl hosszú a szám!")
    else:
        ujszam=0
        while n!=0:
            szj=n%10
            ujszam=ujszam*10+szj
            n=n//10
        print(ujszam)


def feladat24():
    a=0
    b=0
    while True:
        n=int(input('n='))
        if n%7==5:
            a+=1
        elif n%13==7:
            b+=1
        else:
            if n==0:
                break
    print('7-tel való osztási maradéka 5:',a, '13-mal való osztási maradéka 7:',b)


def feladat25():
    fo=float(input('fő:'))
    km=float(input('km:'))
    if fo/km<50:
        print('Ritkán lakott')
    elif fo/km>=50 and fo/km<300:
        print('Átlagon népsűrűség')
    else:
        print('Sűrűn lakott')

def feladat26():
    osszeg=0
    while True:
        n=float(input('szám='))
        osszeg+=n
        if n==0:
            break
    print(osszeg)


def feladat27():
    negativ=0
    pozitiv=0
    x=0
    y=0
    while True:
        n=int(input('szám='))
        if n<0:
            negativ+=1
            x+=1
            y=0
            if x==2:
                break
        elif n>0:
            pozitiv+=1
            y+=1
            x=0
            if x==2 or y==2:
                break
    print('negatív:',negativ, 'pozitív:',pozitiv)


def feladat28(n):
    while n!=0:
        if mt.sqrt(n)==int(mt.sqrt(n)):
            print(n)
            break
        n-=1

def feladat29(n):
    f=1
    if 0<n<=12:
        while n!=0:
            f=f*n
            n-=1
        print(f)


def feladat31(n):
    for i in range(1,(n//2)+1):
        if n%i==0:
            print(i, end=' ')


def feladat32(k, n, m):

    while n<=m:
        if n%k==0:
            print(n)
        n+=1


def feladat36(n):
    a=0
    b=1
    c=a+b
    li=[]
    if c<n and b<n and a<n:
        li.append(a)
        li.append(b)
        li.append(c)
    k = 3
    while k<n:
        a=b
        b=c
        c=a+b
        if c<(n):
            li.append(c)
        k+=1
    print(len(li))

def feladat37(n):
    a=0
    b=1
    c=a+b
    k=3
    while True:
        a=b
        b=c
        c=a+b
        if n==a:
            print(b)
            break


def feladat38(n, szamjegy):
    a=0
    i=1
    n=str(n)
    if len(n)<=9:
        while i<len(n):
            if n[i]==str(szamjegy):
                a+=1
            i+=1
        print(a)




def main():
if __name__=="__main__":
    main()
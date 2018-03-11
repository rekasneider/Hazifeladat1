import math as mt

def feladat_1(n):
    negyoszto=True
    k=0
    for i in range(1,n+1):
        if n%i==0:
            k+=1
    if k!=4:
        negyoszto=False
    return negyoszto


def feladat_3(n):
    k=1
    while n>k:
        k=k*2
    return k


def osztok_szama(szam):
    db=2
    for i in range(2, szam//2+1):
        if szam%i==0:
            db+=1
    return db


def feladat_5(n):
    max=1
    for i in range(2, n+1):
        if max<osztok_szama(i):
            max=osztok_szama(i)
            print(i)

def feladat_10():
    try:
        fajl=open('be.txt', encoding='utf-8', mode='r')
        hossz=0
        for sor in fajl:
            sor=sor.strip()
            if (sor[0].isupper() and len(sor)>hossz):
                hossz=len(sor)
        print(hossz)
    except Exception as e:
        print(e)
    finally:
        fajl.close()


def feladat_11():
    try:
        fajl=open('be.txt', encoding='utf-8', mode='r')
        hossz=mt.inf
        irasjel=['.', '!', '?']
        for sor in fajl:
            sor=sor.strip()
            if (sor[-1] in irasjel and len(sor)<hossz):
                hossz=len(sor)
        print(hossz)
    except Exception as e:
        print(e)
    finally:
        fajl.close()


def feladat_12():
    try:
        fajl1=open('be.txt', mode='r')
        fajl2=open('ki.txt', encoding='utf-8', mode='w')
        li=[]
        a=1
        b=False
        for sor in fajl1:
            sor=sor.strip()
            li.append(sor)
        if len(li)>=1 and len(li)<=15:
            for i in range(len(li)-1):
                if li[i]==li[i+1]:
                    a+=1
                    if a==int(li[-1]):
                        b=True
                        break
                else:
                    a=1
            if b:
                fajl2.write('Tartalmaz egymást követően legalább annyi darab egyforma számot, mint az utoljára beolvasott szám értéke!')
            else:
                fajl2.write('Nem tartalmaz egymást követően legalább annyi darab egyforma számot, mint az utoljára beolvasott szám értéke!')
        else:
            return
    except Exception as e:
        print(e)
    finally:
        fajl1.close()
        fajl2.close()


def feladat_13():
    try:
        fajl=open('be.txt', mode='r')
        a=0
        li=[]
        for sor in fajl:
            sor=sor.strip()
            li.append(sor)
        if len(li) >= 1 and len(li) <= 15:
            for i in range(len(li)-1):
                if abs(int(li[i])-int(li[i+1]))<=int(li[-1]):
                    a+=1
        else:
            return
        print(a)
    except Exception as e:
        print(e)
    finally:
        fajl.close()


def feladat_17():
    try:
        fajl1=open('be.txt', mode='r')
        fajl2=open('ki.txt', encoding='utf-8', mode='w')
        for sor in fajl1:
            sor=sor.strip()
            szo=sor.split(' ')
            for i in range(len(szo)):
                if szo[i].islower():
                    fajl2.write(sor)
                    break
    except Exception as e:
        print(e)
    finally:
        fajl2.close()
        fajl1.close()


def feladat_20():
    try:
        fajl=open('be.txt',encoding='utf-8', mode='r')
        fo=0
        varos=''
        for sor in fajl:
            sor=sor.strip()
            li=sor.split(';')
            for i in li:
                if int(li[2])>fo:
                    fo=int(li[2])
                    varos=li[0]
        print(varos)
    except Exception as e:
        print(e)
    finally:
        fajl.close()


def main():

if __name__=="__main__":
    main()
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



def main():
    feladat_11()
if __name__=="__main__":
    main()
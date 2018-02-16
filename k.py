import codecs as cod
def mehek(n):
    a=1
    b=1
    c=a+b
    if n==1:
        print(a)
    elif n==2:
        print(a, b, end=" ")
    else:
        c=a+b
        print(a,b,c, end=" ")
        k=3
        while k<n:
            a = b
            b = c
            c = a + b
            print(c,end=" ")
            k+=1


def hanyados(n):
    a=1
    b=1
    k=1
    fajl=open("kil.txt", mode="w")
    while k<n:
        fajl.write("%.4f " % (a/b))
        a = a + b
        b = a - b
        k+=1
    fajl.close()


def feladat1(fajl_nev):
    fajl=cod.open(fajl_nev, encoding='utf-8', mode="r")
    max=0
    max_sor=""
    for sor in fajl:
        sor=sor.strip()
        if(sor[0].isupper() and len(sor)>max):
            max=len(sor)
            max_sor=sor
    print(max, max_sor)
    fajl.close()

def feladat2():
    fajl=open("be1.txt", mode="r")
    for sor in fajl:
        if("   " in sor):
            fajl=open("kil.txt", mode='w')
            fajl.write(sor)
            fajl.close()
            break

def fel7(lista, betu):
    li=[]
    fajl=open('ki2.txt', mode='w')
    for i in lista:
        if i[0]==betu:
            li.append(i)
    fajl.write(str(li))
    fajl.close()


def main():
if __name__=="__main__":
    main()

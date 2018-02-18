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


def main():

if __name__=="__main__":
    main()
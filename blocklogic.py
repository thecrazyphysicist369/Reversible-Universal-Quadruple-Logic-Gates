'''print("This is simulating the TNOR gate\n")
print("Enter the following values : \n\n")
A1=int(input("Enter A1 : "))
A2=int(input("Enter A2 : "))
B1=int(input("Enter B1 : "))
B2=int(input("Enter B2 : "))
C1=int(input("Enter C1 : "))
C2=int(input("Enter C2 : "))
L=1'''

def blockpos(L, p1, p2):
    o=0
    if (L==0): #L=00
        o=  0
    if (p1 == 0 and p2 == 0):
        o = 0
    if (p1 == 1 and p2 == 1):
        o = L

    if (L==1): #L=01
        if (p1 == 0 and p2 == 1):
            o = 1
        if (p1 == 1 and p2 == 0):
            o = 0

    if (L == 2):  # L=10
        if (p1 == 0 and p2 == 1):
            o= 0
        if (p1 == 1 and p2 == 0):
            o = 2

    if (L == 3):  # L=11
        if (p1 == 0 and p2 == 1):
            o = 1
        if (p1 == 1 and p2 == 0):
            o = 2
    return o

def blockneg(L, p1, p2):
    p1=complementer(p1)
    p2=complementer(p2)
    if (L==0): #L=00
        o=0

    if ( p1 == 0 and p2 == 0):
        o = 0
    if (p1 == 1 and p2 == 1):
        o = L

    if (L==1): #L=01
        if (p1 == 0 and p2 == 1):
            o = 1
        if (p1 == 1 and p2 == 0):
            o = 0

    if (L == 2):  # L=10
        if (p1 == 0 and p2 == 1):
            o= 0
        if (p1 == 1 and p2 == 0):
            o = 2

    if (L == 3):  # L=11
        if (p1 == 0 and p2 == 1):
            o = 1
        if (p1 == 1 and p2 == 0):
            o = 2
    return o

def beamcombiner (A,B):
    sum=0
    if A!=B:
        sum=3
    if A==0:
        sum= B
    if B==0:
        sum= A
    if A==3 or B==3:
        sum= 3
    if A==B:
        sum=A
    return sum


def complementer(p):
    if p==1:
        return 0
    if p==0:
        return 1


def displayer(R):
    if R == 0:
        print('00')
    if R == 1:
        print('01')
    if R == 2:
        print('10')
    if R == 3:
        print('11')


def beamsplitter(L):
    if L == 0:
        P1=0
        P2=0
    if L == 1:
        P1 = 0
        P2 = 1
    if L == 2:
        P1 = 1
        P2 = 0
    if L == 3:
        P1 = 1
        P2 = 1
    return P1,P2

'''A0=blockpos(L,A1,A2) #Block A
B0=blockpos(L,B1,B2) #Block B
sum = beamcombiner(A0,B0)
v0=subblockspos(L,sum)#Block V
w0=subblockspos(L,sum)#Block W
C0=blockpos(v0,C1,C2) #Block C
x0=subblocksneg(L,w0) #Block X
y0=blockneg(x0,C1,C2) #Block Y
z0=subblockspos(v0,C0) #Block Z
R=beamcombiner(y0,z0)'''



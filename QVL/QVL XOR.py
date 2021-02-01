import blocklogic
print("This is simulating the QUAD valued XOR gate\n")
print("Enter the following values : \n\n")

y='y'
while y == 'y':
    A1 = int(input("Enter A1 : "))
    A2 = int(input("Enter A2 : "))
    B1 = int(input("Enter B1 : "))
    B2 = int(input("Enter B2 : "))
    L=3
    A0=blocklogic.blockpos(L,A1,A2)
    B0=blocklogic.blockpos(A0,B1,B2)
    w0=blocklogic.subblocksneg(A0,B0)
    x0=blocklogic.blockpos(L,A1,A2)
    y0=blocklogic.subblocksneg(L,x0)
    z0=blocklogic.blockpos(y0,B1,B2)
    R=blocklogic.beamcombiner(w0,z0)
    print ('\n\n\n')
    C1,C2=blocklogic.beamsplitter(R)
    print(A1,A2,' XOR ',B1,B2,' = ',C1,C2)

    y = input('\n\nto continue press y   \n')
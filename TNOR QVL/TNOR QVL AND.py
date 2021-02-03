import blocklogic
print("This is simulating the AND gate using RUQLG - TNOR gate\n")
print("Enter the following values : \n\n")

y='y'
while y == 'y':
    A11 = int(input("Enter A1 : "))
    A21 = int(input("Enter A2 : "))
    A12 = int(input("Enter B1 : "))
    A22 = int(input("Enter B2 : "))
    B11 = 0
    B21 = 0
    B12 = 0
    B22 = 0
    C11 = 1
    C21 = 1
    C12 = 1
    C22 = 1
    C13 = 1
    C23 = 1
    L = 3

    A01 = blocklogic.blockpos(L, A11, A21) # Block A
    # print('A0 = ', A0)
    B01 = blocklogic.blockpos(L, B11, B21)  # Block B
    # print('B0 = ',B0)
    sum1 = blocklogic.beamcombiner(A01, B01)
    # print ('sum = ', sum)
    v011, v012 = blocklogic.beamsplitter(sum1)
    v01 = blocklogic.blockpos(L, v011, v012)  # Block V
    # print ('v0 =', v0)
    w011, w012 = blocklogic.beamsplitter(sum1)
    w01 = blocklogic.blockpos(L, w011, w012)  # Block W
    # print('w0 = ',w0)
    C01 = blocklogic.blockpos(v01, C11, C21)  # Block C
    # print('C0 = ',C0)
    x011, x012 = blocklogic.beamsplitter(w01)
    x01 = blocklogic.blockneg(L, x011, x012)  # Block X
    # print('x0 = ',x0)
    y01 = blocklogic.blockpos(x01, C11, C21)  # Block Y
    # print('y0 = ',y0)
    z011, z012 = blocklogic.beamsplitter(C01)
    z01 = blocklogic.blockneg(v01, z011, z012)  # Block Z
    # print('z0 = ',z0)
    R1 = blocklogic.beamcombiner(y01, z01)

    A02 = blocklogic.blockpos(L, A12, A22)  # Block A
    # print('A0 = ', A0)
    B02 = blocklogic.blockpos(L, B12, B22)  # Block B
    # print('B0 = ',B0)
    sum2 = blocklogic.beamcombiner(A02, B02)
    # print ('sum = ', sum)
    v021, v022 = blocklogic.beamsplitter(sum2)
    v02 = blocklogic.blockpos(L, v021, v022)  # Block V
    # print ('v0 =', v0)
    w021, w022 = blocklogic.beamsplitter(sum2)
    w02 = blocklogic.blockpos(L, w021, w022)  # Block W
    # print('w0 = ',w0)
    C02 = blocklogic.blockpos(v02, C12, C22)  # Block C
    # print('C0 = ',C0)
    x021, x022 = blocklogic.beamsplitter(w02)
    x02 = blocklogic.blockneg(L, x021, x022)  # Block X
    # print('x0 = ',x0)
    y02 = blocklogic.blockpos(x02, C12, C22)  # Block Y
    # print('y0 = ',y0)
    z021, z022 = blocklogic.beamsplitter(C02)
    z02 = blocklogic.blockneg(v02, z021, z022)  # Block Z
    # print('z0 = ',z0)
    R2 = blocklogic.beamcombiner(y02, z02)



    A13,A23=blocklogic.beamsplitter(R1)
    B13,B23=blocklogic.beamsplitter(R2)



    A03 = blocklogic.blockpos(L, A13, A23)  # Block A
    # print('A0 = ', A0)
    B03 = blocklogic.blockpos(L, B13, B23)  # Block B
    # print('B0 = ',B0)
    sum3 = blocklogic.beamcombiner(A03, B03)
    # print ('sum = ', sum)
    v031, v032 = blocklogic.beamsplitter(sum3)
    v03 = blocklogic.blockpos(L, v031, v032)  # Block V
    # print ('v0 =', v0)
    w031, w032 = blocklogic.beamsplitter(sum3)
    w03 = blocklogic.blockpos(L, w031, w032)  # Block W1
    # print('w0 = ',w0)
    C03 = blocklogic.blockpos(v03, C13, C23)  # Block C
    # print('C0 = ',C0)
    x031, x032 = blocklogic.beamsplitter(w03)
    x03 = blocklogic.blockneg(L, x031, x032)  # Block X
    # print('x0 = ',x0)
    y03 = blocklogic.blockpos(x03, C13, C23)  # Block Y
    #print('y03 = ',y03)
    z031, z032 = blocklogic.beamsplitter(C03)
    z03 = blocklogic.blockneg(v03, z031, z032)  # Block Z
    #print('z03 = ',z03)
    R = blocklogic.beamcombiner(y03, z03)





    blocklogic.displayer(R)
    y = input('to continue press y   \n')
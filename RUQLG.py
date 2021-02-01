import blocklogic


def RUQLG(L,A,B,C):
    A1, A2 = blocklogic.beamsplitter(A)
    A0 = blocklogic.blockpos(L, A1, A2)  # Block A
    # print('A0 = ', A0)
    B1, B2= blocklogic.beamsplitter(B)
    B0 = blocklogic.blockpos(L, B1, B2)  # Block B
    # print('B0 = ',B0)
    sum = blocklogic.beamcombiner(A0, B0)
    # print ('sum = ', sum)
    v1, v2 = blocklogic.beamsplitter(sum)
    v0 = blocklogic.blockpos(L, v1, v2)  # Block V
    # print ('v0 =', v0)
    w1, w2 = blocklogic.beamsplitter(sum)
    w0 = blocklogic.blockpos(L, w1, w2)  # Block W
    # print('w0 = ',w0)
    C1, C2 = blocklogic.beamsplitter(C)
    C0 = blocklogic.blockpos(v0, C1, C2)  # Block C
    # print('C0 = ',C0)
    x1, x2 = blocklogic.beamsplitter(w0)
    x0 = blocklogic.blockneg(L, x1, x2)  # Block X
    # print('x0 = ',x0)
    y0 = blocklogic.blockpos(x0, C1, C2)  # Block Y
    # print('y0 = ',y0)
    z1, z2 = blocklogic.beamsplitter(C0)
    z0 = blocklogic.blockneg(v0, z1, z2)  # Block Z
    # print('z0 = ',z0)
    R = blocklogic.beamcombiner(y0, z0)
    return A0, B0, R
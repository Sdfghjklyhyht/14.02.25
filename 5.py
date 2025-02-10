for N in range(256):
    R=bin(N)[2:]
    if len(R)<8:
        R='0'*(8-len(R))+R
    x=R[:2]+R[-2:]
    x=int(x,2)
    if N<110:
        if x==7:
            print(N,x)

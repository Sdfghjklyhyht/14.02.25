def f(a,b,c):
     if a*b>c:
         return 1
     else:
         return 0
for A in range(-1000,1000):
    z=1
    for x in range(200):
        for y in range(200):
            if (f(x,y,A+13) or f(28,y,520) or f(x,25,800))==0:
                z=0
            else:
                pass
    if z==1:
        print(A)

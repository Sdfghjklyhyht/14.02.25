def d(x,y):
    a=[]
    if x<10 or y<10:
        return []
    if int(str(x)[0]+str(y)[0])<x:
        a.append((int(str(x)[0]+str(y)[0]),y))
    if int(str(x)[1] + str(y)[0]) < x:
        a.append((int(str(x)[0] + str(y)[0]), y))
    if int(str(x)[1] + str(y)[1]) < x:
        a.append((int(str(x)[1] + str(y)[1]), y))
    if int(str(x)[0] + str(y)[1]) < x:
        a.append((int(str(x)[0] + str(y)[1]), y))
    if int(str(y)[0]+str(x)[0])<y:
        a.append((x,int(str(y)[0]+str(x)[0])))
    if int(str(y)[1]+str(x)[0])<y:
        a.append((x,int(str(y)[1]+str(x)[0])))
    if int(str(y)[1]+str(x)[1])<y:
        a.append((x,int(str(y)[1]+str(x)[1])))
    if int(str(y)[0]+str(x)[1])<y:
        a.append((x,int(str(y)[0]+str(x)[1])))
    return a

def f(x,y,p):
    if len(d(x,y))==0 and p==3: return True
    if len(d(x, y)) != 0 and p == 3: return False
    if len(d(x, y)) == 0 and p != 3: return False
    if p%2==0:
        r=False
        for i in d(x,y):
            r=r or f(i[0],i[1],p+1)
        return r
    else:
        r = True
        for i in d(x, y):
            r = r and f(i[0], i[1], p + 1)
        return r
for x in range(10,100):
    for y in range(10,100):
        if f(x,y,1):
            print(x,y)

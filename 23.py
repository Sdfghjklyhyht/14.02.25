def p(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k+=1
    if k==0:
        return 1
    else:
        return 0
def d(n):
    k=0
    for i in range(n+1,1000):
        if p(i):
            k=i
            break
    return k
def f(x,y):
    if x==y:
        return 1
    if x>y or x==33:
        return 0
    if x<y:
        return f(x+2,y)+f(d(x),y)
print(f(2,14)*f(14,45))

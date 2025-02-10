from fnmatch import fnmatch

for n in range(10**7):
    i=int('32'+str(n)+'123')
    if i%519==0:
        if fnmatch(str(i),'32*54?123'):
            a=0
            b=0
            if len(str(i))%2==0:
                if str(i).count('0')==0:
                    for x in range(len(str(i))//2):
                        a+=int(str(i)[x])
                    for y in range(len(str(i))//2,len(str(i))):
                        b+=int(str(i)[y])
                    if a==b:
                        print(i, i//519)

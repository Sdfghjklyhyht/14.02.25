x=7**500+7**200-7**50s=''
while x>0:
    ost=x%7    
    s+=str(ost)
    x=x//7
    s=s[::-1]
print(s)
z=s.replace('0','6')
z=z[1:]
print(z)
print(z.count('6')*6)

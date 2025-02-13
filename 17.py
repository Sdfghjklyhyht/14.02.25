s=open('17.txt').readlines()
for i in range(len(s)):
    s[i]=int(s[i])
print(len(s))
mx=0
mn=100000000000000
for i in range(len(s)):
    mn=min(mn,s[i])
    mx=max(mx,s[i])
sr=(mn+mx)/2
k=0
mx1=-1000000
for i in range(len(s)//2):
    x=len(s)
    if (s[i]<sr and s[x-i-1]>sr) or (s[i]>sr and s[x-i-1]<sr):
        k+=1
        mx1=max(mx1, s[i]+s[x-1-i])
print(k,mx1)

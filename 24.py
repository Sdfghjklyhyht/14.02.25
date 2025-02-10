s=open('24.txt').readline()
print(s)
mx=-100000000000000
k=0
x=0
for i in range(len(s)):
    if s[i]!=s[i-1] and k==0:
        k+=1
        x=s[i-1]
    if k>0 and s[i]==s[i-1]:
        k+=1
    if k>0 and s[i]!=s[i-1]:
        if s[i]==x:

            mx=max(mx,k)
            k=1
            x=s[i]
        else:
            k = 1
            x = s[i-1]
    if k==5:
        print(s[i])
print(mx)

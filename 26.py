s=open('26 (2).txt').readlines()
s.pop(0)
for i in range(len(s)):
    s[i]=s[i].split()
    s[i][0]=int(s[i][0])
    s[i][1] = int(s[i][1])
    s[i][1] = s[i][0]-(s[i][1]*2)
s.sort(key=lambda x:x[1])
s.reverse()

a=[401]
for i in range(len(s)):
    if s[i][0]<=(a[-1])-3:
        a.append(s[i][1])

print(len(a)-1)
a=[401]
mx=-1000000000
for i in range(len(s)):
    if s[i][0]<=(a[-1])-3 and len(a)<36:
        a.append(s[i][1])
    if len(a)==36 and s[i][0]<=(a[-1])-3:
        if mx<s[i][0]:
            mx=s[i][0]
print(mx)

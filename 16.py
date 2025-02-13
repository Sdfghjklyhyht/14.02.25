import sys
sys.setrecursionlimit(1000000)
from functools import lru_cache
@lru_cache()
def f(n):
    if n>=3210:
        return 1
    if n<3210:
        return f(n+3)+7
def g(n):
    if n<10:
        return n
    if n>=10:
        return g(n-3)+5
for i in range(3210,15,-1):
    f(i)
for i in range(3000,10,-1):
    g(i)
print(f(15)-g(3000))

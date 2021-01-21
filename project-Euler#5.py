#here we have to import a math module called gcd(greatest common divisor)to finf LCM
from math import gcd
def LCM(a , b):
#this is the formula to find LCM W.r.t of gcd  (for ex : gcd of 4 & 6 is 2)    
    return  (a * b) // gcd(a, b)


t = int(input())
for _ in range(t):
    N = int(input())
    lcm = 1
    for i in range(1 , N+1):
    #so here we taken it from 1 , N+ 1 according to question    
        lcm = LCM(lcm , i)
    print(lcm)

#this is some what tricky question for beginners because they told to find  a number which is divisble by by all digits given in that range
#that actually means we have to find the lcm of all that reumber 

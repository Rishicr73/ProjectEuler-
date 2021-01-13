#!/bin/python3
import sys
 
t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    
    three = int((n-1)/3) #gives count of numbers divisible by 3 upto (n-1)
    five = int((n-1)/5) #gives count of numbers divisible by 5 upto (n-1)
    fifteen = int((n-1)/15) #gives count of numbers divisible by 15 upto (n-1)
    
    #sum of arithmetic equation formula = n/2(2a + (n - 1)d)
    #here a == d
    #so we  can write this formula as = (a * n * (n-1))/2
    
    sum_ = (3 * three * (three + 1)) // 2 + (5 * five * (five + 1)) // 2 - (15 * fifteen * (fifteen + 1)) // 2
    
    print(sum_)             
    


    
        


    

        
    
    
   
   




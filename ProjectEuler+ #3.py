 
 
#!/bin/python3

import sys


T = int(input())
for z in range(T):
    N = int(input())
    i = 2
    largest_prime = 2
    while i * i <= N:   #here we have taken i*i to reduce time complexity
        while N % i == 0:
            largest_prime = i
            N //= i    
        i += 1
    if N>largest_prime:
        largest_prime = N
    print(largest_prime)         


        
          
        
        

    




        
            

  


    


    
        


    

        
    
    
   
   




t = int(input())
sum_ = 0
for i in range(t):
    n = int(input())
    sum_ += n
sum = str(sum_)  #Here we have taken str function to do slicing in next method so 
#we can get the number upto which we want. int() fuction slicing not possible
print(sum[:10])  
#Here we have taken slicing method 
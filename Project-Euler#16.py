#POWER DIGIT SUM

t = int(input())
for a0 in range(t):
    n = int(input())
    r = str(2**n)  #HERE WE HAVE STR FUNCTION BECAUSE WE WANT TO USE THAT NUMBER IN NEXT FOR LOOP SO IT WILL TAKE ON ON ELEMENT OF R
                   #WE DON'T GIVE STR FUNCTION THEN ITS ALREADY A INTEGER FUNCTION SO IT WILL TAKE ONLY ONE ELEMENT THAT' THE SQUARE OF R SO WE GET ERROR
    sum_ = 0
    for i in r:
        sum_ += int(i)

    print(sum_)    

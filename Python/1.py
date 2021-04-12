import math

def twinprime(n):
    
    n=10 ** n
    prime = [True for i in range(n + 2)]
    p = 2
     
    while (p * p <= n + 1):
        if (prime[p] == True):
            for i in range(p * 2, n + 2, p):
                prime[i] = False
        p += 1
    for p in range(2, n-1):
        if prime[p] and prime[p + 2]:
            a=str(p)
            b=str(p+2)
            file.write("(")
            file.write(a)
            file.write(",")
            file.write(b)
            file.write(") ")
    
   
 
 
# driver program
if __name__=='__main__':
    val=int(input())
    file = open("myFirstFile.txt", "a")
    twinprime(val)
    file.close()
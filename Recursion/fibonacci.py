#The Fibonacci series is the sequence where each number is
#  the sum of the previous two numbers of the sequence. 
# The first two numbers of the Fibonacci series are 0 and 1 
# and are used to generate the Fibonacci series.

#---> Define a fibonacci function

def fib(i):
    #Base Case
    if(i==0 ): #The 0th Fibonacci number is 0.
        return 0
    
    if(i==0 or i == 1): #1st Fibonacci number = 1 & 2nd Fibonacci number = 1
                        
         return 1
    
    #recursive case

    return (fib(i-1) + fib(i-2))

def main():
    n=int(input("Enter a fibonacci no : "))
    for i in range(0,n):
        print(fib(i))

main()







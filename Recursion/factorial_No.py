
def fact(n):
    #Base case
    if n==1:
        return 1
    
    #recursive case
    return n * fact(n-1)

def main():
    n=int(input("Enter factorial number : "))
    print(fact(n))
main()


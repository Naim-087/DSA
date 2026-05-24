def alternate(myArr,n):
    print('\n')
    for i in range(0,n,2):
        print(myArr[i])
    
def main():
    n=int(input("Enter array size : "))
    arr = []
    #take array input
    for x in range(n):
        x=int(input())
        arr.append(x)

    alternate(arr,n)

main()
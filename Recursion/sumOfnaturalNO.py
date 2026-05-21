
def sum(n):

    # Base case
    if n == 1:
        return 1

    # Recursive case
    return n + sum(n - 1)


def main():

    n = 5
    print(sum(n))


main()
while True:
    print('Enter a number to see if it is a prime number')
    n = input()
    n = int(n)
    for i in range (2, n):
        if(n % i == 0):
            print('This is not a prime number!')
            break
    else:
            print(n, ' is a prime number!')
            break

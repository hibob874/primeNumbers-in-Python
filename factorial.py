while True:
    print('Hello there! Enter a number to get the result of its factorial!')
    n = input()
    n = int(n)
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial*i
    print('The factorial of ', n, 'is ', factorial)

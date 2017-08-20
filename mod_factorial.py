def factorial(x):
    result = 1
    for i in range(1, x+1):
        result = result * i
    print('Factorial of number '+ str(x) + ' is equal ' + str(result))

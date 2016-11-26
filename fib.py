def get_fibs(n):
    fib = [0,1]
    sum = 0

    for i in range(2,n):
        sum = fib[i-1] + fib[i-2]
        fib.append(sum)

    return fib

print(get_fibs(100))

def fib(f,n):
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    return f

f=[0,1]
print(fib(f,10))
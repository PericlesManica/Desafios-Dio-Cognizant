n = int(input())
fib_list = []
n = n - 1
for i in range(0, n+1):
    if i < 2:
        fib_list.append(i)
    else:
        fib_list.append(fib_list[i-1]+fib_list[i-2])
fib_string = ' '.join([str(n) for n in fib_list])
print(fib_string)

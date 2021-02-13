import time 

###  iteration  ###
def fib(n):         # Complexity = O(n)
    arr = list()
    arr.append(0)
    arr.append(1)
    for i in range(n):
        arr.append(arr[i]+ arr[i+1])
        print(i, arr[i])


###   recursion   ###
def recursvfib(n):      # Complexity = O(2^n)
    if n <= 1:
        return n
    else:
        return recursvfib(n-1) + recursvfib(n-2)


def recursvfib_main(n):
    for i in range(n):
        print(recursvfib(i))


###   main   ###
inpt = input()
inpt = int(inpt)
start_time_iter = time.time()
fib(inpt)
end_time_iter = time.time()
start_time_recur = time.time()
recursvfib_main(inpt)
end_time_recur = time.time()
print("Time for iteration:", (end_time_iter - start_time_iter)*1000,"ms\nTime for recursion:", (end_time_recur - start_time_recur)*1000, "ms")

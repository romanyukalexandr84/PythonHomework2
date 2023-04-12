n = int(input("Введите число n: "))
step = 1
i = 1
while step < n:
    print(step, end=" ")
    step = 2**i
    i += 1

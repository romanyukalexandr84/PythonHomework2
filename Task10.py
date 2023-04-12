import random
n = int(input("Введите количество монеток: "))
zeros = 0
ones = 0
for i in range(0, n):
    side = random.randint(0, 1)
    print(side, end=" ")
    if side == 0:
        zeros += 1
    else:
        ones += 1
print()
if zeros <= ones:
    print("Минимальное количество монет, которые нужно перевернуть =", zeros)
else:
    print("Минимальное количество монет, которые нужно перевернуть =", ones)

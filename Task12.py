x = 1001
y = 1001

while x > 1000 or y > 1000:
    s = int(input("Введите сумму двух натуральных чисел x и y (каждое <=1000): "))
    p = int(input("Введите произведение двух натуральных чисел x и y: "))
    x = int((-s + (s*s-4*p)**0.5) / -2)
    y = s-x

print ("Число x = ",x)
print ("Число y = ",y)
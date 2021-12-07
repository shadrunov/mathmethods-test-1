import math
y = int(input("Z = "))
x = int(input("X = "))

def order(x, y):
    n = 0
    for i in range(1, y):
        num = (x ** i) % y
        if (num == 1):
            n += 1
        if (num == 1 and n == 2):
            break
        print (num)

print('First part:')
n = 0
for i in range(1, y):
    if math.gcd(i, y) == 1:
        print(i)
    n += 1
print('n =', n)

# begin after first "1" appears

print('Second part:')
order(x, y)

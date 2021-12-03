import math

print('Задание 3. Изучить кольцо классов вычетов Z_k')
k = int(input('Введите k: '))
# k = 32

# 1 
ring = [i for i in range(k)]
print(f'Множество классов вычетов Z_{k} = {{{", ".join(map(str, ring))}}} \n')

# 2
ring_star = [i for i in ring if math.gcd(i, k) == 1]
print(f'Кольцо классов вычетов Z^*_{k} = {{{", ".join(map(str, ring_star))}}}')

print(f'| Z^*_{k} | = {len(ring_star)} \n')

# 3
left = ring_star.copy()
used = [1]

h_counter = 1

for el in left:
    if el in used:
        continue

    print(f'\n\n{el}: ')
    h = [1, el]
    i = 1
    while(el ** i % k != 1):
        i += 1
        print(f'{el}^{i} = {(el ** (i-1) % k) * el} mod {k} = {el ** i % k}')
        h.append(el ** i % k)
    h.pop()

    # print(f'порядок элемента O({el}) = {len(h)} \n')
    print(f'H_{h_counter} = <{el}> = {{{", ".join(map(str, h))}}}')
    h_counter += 1

    orders = {}
    print('порядки элементов: ')
    for elh in h:
        if elh not in used:
            o = math.gcd(h.index(elh), len(h))
            p = len(h) // o
            if o != 1 and o != len(h):
                print(f'O({elh}) = {len(h)}/НОД({h.index(elh)}, {len(h)}) = {p}')
            else:
                print(f'O({elh}) = {p}')

            if orders.get(p):
                orders[p].append(elh)
            else:
                orders[p] = [elh]
        used.append(elh)
    
    if len(orders[len(h)]) > 1:
        print(f'H_{h_counter - 1} = <{"> = <".join(map(str, orders[len(h)]))}>')
    
    for p in orders:
        if p != len(h):
            x = orders[p][0]
            new_h = [1, x]
            i = 1
            while(x ** i % k != 1):
                i += 1
                new_h.append(x ** i % k)
            new_h.pop()
            print(f'H_{h_counter} = <{"> = <".join(map(str, orders[p]))}> = {{{", ".join(map(str, new_h))}}}')
            h_counter += 1

# def order(x, y):
#     n = 0
#     for i in range(1, y):
#         num = (x ** i) % y
#         if (num == 1):
#             n += 1
#         if (num == 1 and n == 2):
#             break
#         print (num)

# print('First part:')
# n = 0
# for i in range(1, y):
#     if math.gcd(i, y) == 1:
#         print(i)
#     n += 1
# print('n =', n)

# # begin after first "1" appears

# print('Second part:')
# for i in range(1, y):
#     if math.gcd(i, y) == 1:
#         order(i, y)
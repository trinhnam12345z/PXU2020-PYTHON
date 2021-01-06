import random

n = int(input('Nhap n :'))
# x = random.uniform(10,99)
# print(x)
list = []
for item in range(n):
    a = float(random.uniform(10,99))
    list.append(a)
print('List = ',list)
min = list[0]
for item in list:
    if item < min :
        min = item
print('Gia tri nho nhat cua list la :',min)

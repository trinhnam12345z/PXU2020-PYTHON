import random

n = int(input('Nhap n :'))
list = random.sample(range(10,99),n)
max = 0
for item in list:
    if item > max :
        max = item
print('List = ',list)
print('Gia tri lon nhat cua list la :',max)

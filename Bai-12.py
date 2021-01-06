import random

print('Câu 1 : Tạo 1 số nguyên ngẫu nhiên n trong khoảng [50, 1000] đóng vai trò là số phần tử của List')
n = random.randrange(50,1000)
print('n = ' , n)
print('Câu 2 : Sinh ngẫu nhiên 1 List các số nguyên trong khoảng [-1000, 1000]')
list_int = random.sample(range(-1000,1000),n)
print('List-int = ',list_int)
print('Câu 3 : Sinh ngẫu nhiên 1 List các số thực trong khoảng [-1000.0, 1000.0]')
list_float =[]
for item in range(n):
    a = float(random.uniform(-1000,1000))
    list_float.append(a)
print('List-float = ',list_float)
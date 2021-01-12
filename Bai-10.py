import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 1 .
print("================================================")
print("1.")
_A = [[1, 2, 3], [4, 5, 6]]
_B = [[6, 5, 4], [3, 2, 1]]
A = np.array(_A)
B = np.array(_B)
print('A = ')
print(A)
print('B = ')
print(B)
print('A + B =')
print(A + B)
print('A * B =')
print(A * B)
print('Chuyển vị A :')
print(A.transpose())
print('Chuyển vị B :')
print(B.transpose())
print("================================================")
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# 2 .
print("2.")
#đọc từ máy
a = pd.read_excel("E:\Python\Book1.xlsx")
print(a)
print("================================================")
# đọc từ internet
url = r'https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv'
df = pd.read_csv(url)
print(df)
print("================================================")
print("3.")

x = [2, 4, 6]
y = [4, 3, 5]

#Vẻ biểu đồ
plt.plot(x, y)
plt.boxplot(x, y)
plt.bar(x,y)
plt.show()




b = [('Join' , 12), ('Hung', 15),('Nam',20)]
for  item in b:
    print(item)
print('--------------')
a = 15
b = 7
# print('a = ' ,a,'b = ',b )
# a,b=b,a
# print('a = ' ,a,'b = ',b )
print(a,b)
def hoan_doi(a,b):
    a, b = b, a
    return a ,b

a ,b=hoan_doi(a,b)
print(a,b)
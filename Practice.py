#print(round(123.456,2))

'''a= [1,2,3,4,5,6,7,8,9]
print(a)

print(a[4])

a = list()
print(a)'''

#크기가 N이고 모든 값이 1인 리스트 초기화

"""n = 5
a = [1] * n
print(a)"""

'''array = []
print(array)
for i in range(20):
    if i % 2 == 1:
        array.append(i)
'''

#리스트 컴프리헨션 == 리스트를 초기화 하는 방법
array = [i for i in range(20) if i % 2 ==1]
print(array)

array = [i * i]
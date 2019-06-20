number = int(input())

array = list(map(int, input().split()))

index_min = array.index(min(array))
index_max = array.index(max(array))

amount = 0
for element in array:
    if element > 0:
        amount += element

if index_min > index_max:
    index_min, index_max = index_max, index_min

multiplication = 1
for i in array[index_min + 1:index_max]:
    multiplication *= i

print(amount, multiplication)

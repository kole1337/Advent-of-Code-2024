def distance(arr1, arr2) -> int:
    arr1.sort()
    arr2.sort()
    sum = 0
    for i in range(len(arr1)):
        sum += abs(arr1[i] - arr2[i])

    return sum

def similarity(arr1, arr2) -> int:
    arr1.sort()
    arr2.sort()
    sims = 0
    count = 0
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if arr1[i] == arr2[j]:
                count = count + 1
            sims += (arr1[i] * count)
            count = 0

    return sims


input1 = []
while True:
    try:
        ass = input().split()
        # print(ass[0])
    except EOFError:
        break
    input1.append(ass[0])
    input1.append(ass[1])
for i in range(len(input1)):
    input1[i] = int(input1[i])


input2 = []
input3 = []

for i in range(len(input1)):
    if i%2==0:
        input2.append(input1[i])
    else:
        input3.append(input1[i])
# print(f'{len(input1)}, {len(input2)}, {len(input3)}')

print(similarity(input2,input3))
# print(f'{len(input2)} and {len(input3)}')
# print(distance([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]))


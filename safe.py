def safeCode(arr1):
    checkSafe = []
    isSafe = False
    dec = False
    n = len(arr1) - 1
    fault = 0
    if arr1[0] > arr1[1]:
        dec = True

    # print(f"Is arr decreasing: {dec}")
    i = 0
    while i < n:
        print(f"faults: {fault}")
        # print(f"i:{i} and n:{n}")
        # check if array is strictly decreasing
        if dec:
            if arr1[i] > arr1[i+1]:
                if 1 >= arr1[i]-arr1[i+1] or arr1[i]-arr1[i+1] <= 3:
                    # print(arr1[i]-arr1[i+1])
                    checkSafe.append(True)
                    print("Safe protocol")
                    i+=1
                else:
                    arr1.pop(i)
                    fault += 1

                    if arr1[i] > arr1[i+1]:
                        if 1 >= arr1[i] - arr1[i+1] or arr1[i] - arr1[i+1] <= 3:
                        # print(arr1[i]-arr1[i+1])
                            print("Unsafe protocol")
                            n -= 1
                            i-=1
                            checkSafe.append(True)
                        else:
                            print("Break protocol")
                            checkSafe.append(False)
                            break
            else:
                arr1.pop(i)
                print(arr1)
                i -= 1
                if arr1[i-1] > arr1[i]:

                    if 1 >= arr1[i-1] - arr1[i] or arr1[i-1] - arr1[i] <= 3:
                        # print(arr1[i]-arr1[i+1])
                        n -= 1
                        print("Unsafe protocol")
                        fault += 1
                        checkSafe.append(True)
                    else:
                        print("Break protocol")

                        checkSafe.append(False)
                        break
                print(f"i:{i}")
        # if array is strictly increasing
        else:
            print(f"i:{i} and n:{n}")
            if arr1[i] < arr1[i+1]:
                # Safe protocol
                if 1 >= abs(arr1[i]-arr1[i+1]) or abs(arr1[i]-arr1[i+1]) <= 3:
                    # print(arr1[i]-arr1[i+1])
                    checkSafe.append(True)
                    print("Safe protocol")
                    i+=1
                    # print("App true")
                else:
                    arr1.pop (i)
                    fault += 1
                    if not i < 0:
                        i -= 1

                    if arr1[i - 1] < arr1[i]:
                        if 1 >= abs(arr1[i - 1] - arr1[i]) or abs(arr1[i - 1] - arr1[i]) <= 3:
                            # print(arr1[i]-arr1[i+1])
                            print("Unsafe protocol")
                            n -= 1
                            checkSafe.append(True)
                        else:
                            print("Break protocol")
                            checkSafe.append(False)
                            break
            else:
                arr1.pop(i)
                print(arr1)
                if not i < 0:
                    i -= 1
                fault += 1
                print(f"ELSE I: {i}")
                if arr1[i] < arr1[i+1]:
                    if 1 >= abs(arr1[i] - arr1[i+1]) or abs(arr1[i] - arr1[i+1]) <= 3:
                        # print(arr1[i]-arr1[i+1])
                        n -= 1
                        print("Unsafe protocol")
                        checkSafe.append(True)
                    else:
                        print("Break protocol")

                        checkSafe.append(False)
                        break
        # print(f'i: {i}')
        # if arr1[i] < arr1[i+1]:
        #     if 1 >= arr1[i]-arr1[i+1] <= 3:
        #         sum+=1



    # check if any of the elements are strictly decreasing in the array
    # ie False means that a < b
    for i in range(len(checkSafe)):
        if not checkSafe[i]:
            isSafe = False
            break
        else:
            isSafe = True

    return isSafe

codes = []
while True:
    try:
        acc = input().split()
        for i in range(len(acc)):
            acc[i] = int(acc[i])
        codes.append(acc)
    except EOFError:
        break
print(f'{len(codes)} codes')
sum = 0
for i in codes:
    if safeCode(i):
        sum+=1

print(f'{sum} safe protocols')
# print(safeCode([7,6,4,1,0]))
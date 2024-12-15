def runningSum( nums: list[int]) -> list[int]:
    sum = 0
    xs = nums.copy()
    for i in range(len(nums)):
        for j in range(i+1):
            sum = sum + xs[j]
        nums[i] = sum
        sum = 0

    return nums


print(runningSum([1,2,3,4]))
# 1,2,3,4,5

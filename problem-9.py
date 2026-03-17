nums = [2, 7, 11, 15]
target = 9

d = {}

for i in range(len(nums)):
    rem = target - nums[i]
    if rem in d:
        print([d[rem], i])
        break
    d[nums[i]] = i
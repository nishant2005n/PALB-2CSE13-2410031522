arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

if arr[0] == 0:
    print(-1)

maxReach = arr[0]
step = arr[0]
jump = 1

for i in range(1, len(arr)):
    if i == len(arr) - 1:
        print(jump)
        break
    maxReach = max(maxReach, i + arr[i])
    step -= 1
    if step == 0:
        jump += 1
        if i >= maxReach:
            print(-1)
            break
        step = maxReach - i
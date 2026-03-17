arr = [1, 4, 45, 6, 10, 8]
target = 13

arr.sort()
found = False

for i in range(len(arr)-2):
    l = i + 1
    r = len(arr) - 1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        if s == target:
            print("Triplet found:", arr[i], arr[l], arr[r])
            found = True
            break
        elif s < target:
            l += 1
        else:
            r -= 1
    if found:
        break

if not found:
    print("No triplet found")
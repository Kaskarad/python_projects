tracker = dict()

nums = [1, 2, 5 ,7]
target = 12
for i, val in enumerate(nums):

    rem = target - val

    if rem in tracker:
        print([tracker[rem], i])

    tracker[val] = i

print([])
import two_sum_long_input as tsli

def brut_two_sum(nums, target):
    print(f"calculating two sum for {nums} with target: {target}")
    res = []
    for (i, n1) in enumerate(nums):
        print(f"outer loop at index {i} and val {n1}")

        next = i + 1
        # index out of bounds prevention
        if next == len(nums):
            break

        # last value not included in slice. thus keeping it len(nums)
        # for e.g. range(1,5) means 1 till 4
        slice = nums[next:len(nums)]

        for (j, n2) in enumerate(slice, next):
            print(f"inner loop at index {j} and val {n2}")
            total = n1 + n2
            if total == target:
                res = [i, j]
                return res
            else:
                continue
    return res

assert [3,4] == brut_two_sum(tsli.long_input, tsli.long_input_target)

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = len(nums)//2
    left, right, equal = [], [], []
    for i in range(len(nums)):
        if nums[i] < nums[pivot]:
            left.append(nums[i])
        elif nums[i] > nums[pivot]:
            right.append(nums[i])
        else:
            equal.append(nums[i])
    left = quicksort(left)
    right = quicksort(right)
    return left + equal + right

print quicksort([5,2,46,8,5,23,435,1])

def weirdsort(nums):
    i = len(nums)
    for idx, num in enumerate(nums):
        if num >= 0:
            i = idx
            break
    pivot = nums[i]
    j = i + 1
    while j < len(nums):
        if nums[j] < 0 and j == i+1:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            i += 1
        elif nums[j] >= 0:
            k = j
            j += 1
            if j >= len(nums):
                break
            while nums[i+1] >= 0 and j < len(nums) and k < len(nums):
                print "-swapping", nums[k], nums[j]
                nums[k], nums[j] = nums[j], nums[k]
                j += 1
                k += 1
                if j >= len(nums):
                    break
            j = i+1
    nums[i] = pivot
    return nums


print weirdsort([-1, 3, 2, -1])
print weirdsort([-1, 1, -2, 3, -4, -5, 7, 8])

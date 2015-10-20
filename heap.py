def heapsort(nums):
    heapify(nums, 0, len(nums))
    for i in range(len(nums)-1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i)
    return


def heapify(nums, start, end):
    mid = (end-start)//2
    for i in range(mid, -1, -1):
        sift_down(nums, i, end-1)
    return


def sift_down(nums, node, end):
    max_i = left = node*2+1
    right = left + 1

    if left > end:
        return

    if right <= end:
        if nums[right] > nums[left]:
            max_i = right

    if nums[node] < nums[max_i]:
        nums[node], nums[max_i] = nums[max_i], nums[node]
        sift_down(nums, node, end)

    return

nums = [46, 52, 28, 1, 2]
heapsort(nums)
print nums

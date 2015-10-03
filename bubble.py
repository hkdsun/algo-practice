def bubble(nums, n):
    for i in range(n-1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


def insertion(nums, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            print j
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
        print "done"


def heapify(nums, root, end):
    i = root
    ileftchild = 2*i + 1
    irightchild = 2*i + 2

    if ileftchild < end and irightchild < end:
        if nums[i] < nums[ileftchild] or nums[i] < nums[irightchild]:
            j = 0
            if nums[ileftchild] > nums[irightchild]:
                j = ileftchild
                nums[i], nums[ileftchild] = nums[ileftchild], nums[i]
            else:
                j = irightchild
                nums[i], nums[irightchild] = nums[irightchild], nums[i]
            heapify(nums, j, end)
    elif ileftchild < end:
        if nums[i] < nums[ileftchild]:
            nums[i], nums[ileftchild] = nums[ileftchild], nums[i]


def heapsort(nums):
    n = len(nums)

    for i in range(n/2, -1, -1):
        heapify(nums, i, len(nums))

    for i in range(n-1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0, i)

    print nums


def mergelists(nums1, nums2):
    i1, i2 = 0, 0
    res = []
    while(i1 < len(nums1) and i2 < len(nums2)):
        if nums1[i1] <= nums2[i2]:
            res.append(nums1[i1])
            i1 += 1
        else:
            res.append(nums2[i2])
            i2 += 1
    if i1 < len(nums1):
        while i1 < len(nums1):
            res.append(nums1[i1])
            i1 += 1
    else:
        while i2 < len(nums2):
            res.append(nums2[i2])
            i2 += 1
    return res


def mergesort(nums):
    if not nums:
        return []
    if len(nums) == 2:
        return mergelists([nums[0]], [nums[1]])
    else:
        n = len(nums)/2
        return mergelists(mergesort(nums[:n]), mergesort(nums[n:]))


def median(nums, l, m, h):
    if nums[l] < nums[m]:
        return m if nums[m] < nums[h] else h
    else:
        return l if nums[l] < nums[h] else h


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        more = []
        less = []
        equal = []
        pivot = nums[len(nums)/2]
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                more.append(i)
        more = quicksort(more)
        less = quicksort(less)
        return less + equal + more


n = [1, 5, 2, 25, 35, 3, 12, 30]
print quicksort(n)

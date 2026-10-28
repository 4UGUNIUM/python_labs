def linear_search(nums, x):
    """Первый индекс x или -1."""
    for i, value in enumerate(nums):
        if value == x:
            return i
    return -1


def binary_search(sorted_nums, x):
    """Индекс x или -1. На неотсортированном списке результат не определён."""
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        if sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None


def two_sum_fast(nums, target):
    seen = {}
    for j, value in enumerate(nums):
        if target - value in seen:
            return seen[target - value], j
        seen[value] = j
    return None

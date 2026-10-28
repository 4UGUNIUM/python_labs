def bubble_sort(nums):
    """Новый отсортированный список, исходный не меняется."""
    result = list(nums)
    for end in range(len(result) - 1, 0, -1):
        changed = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                changed = True
        if not changed:
            break
    return result


def insertion_sort(nums):
    """Новый отсортированный список."""
    result = list(nums)
    for i in range(1, len(result)):
        value = result[i]
        j = i - 1
        while j >= 0 and result[j] > value:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = value
    return result


def selection_sort(nums):
    """Новый отсортированный список."""
    result = list(nums)
    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result

import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100):
    cases = [[], [1], [2, 2, -1], [1, 2, 3], [3, 2, 1]]
    cases += [[random.randint(-100, 100) for _ in range(random.randint(0, 50))]
              for _ in range(trials)]
    for nums in cases:
        original = nums.copy()
        result = fn(nums)
        assert result == sorted(nums), (fn.__name__, nums, result)
        assert nums == original and result is not nums, (fn.__name__, original)


def check_search():
    cases = [[], [1], [1, 1], [2, 1]]
    cases += [[random.randint(-100, 100) for _ in range(random.randint(0, 50))]
              for _ in range(100)]
    for nums in cases:
        ordered = sorted(nums)
        for x in [-101, 101, 0] + nums:
            expected = nums.index(x) if x in nums else -1
            assert linear_search(nums, x) == expected, (nums, x)
            index = binary_search(ordered, x)
            assert (index == -1 if x not in ordered else
                    0 <= index < len(ordered) and ordered[index] == x), (ordered, x, index)


def check_two_sum(trials=100):
    cases = [([], 0), ([1], 2), ([3, 3], 6), ([1, 2], 10)]
    cases += [([random.randint(-100, 100) for _ in range(random.randint(0, 50))],
               random.randint(-200, 200)) for _ in range(trials)]
    for nums, target in cases:
        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)
        assert (brute is None) == (fast is None), (nums, target, brute, fast)
        for pair in (brute, fast):
            if pair is not None:
                i, j = pair
                assert 0 <= i < j < len(nums) and nums[i] + nums[j] == target, (nums, target, pair)


if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK: 523 проверок наборов данных")

#Мин макс 

def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает минимальный и максимальный элементы списка."""
    if len(nums) == 0:
        raise ValueError("Пустой список")

    min_num = nums[0]
    max_num = nums[0]

    for num in nums[1:]:
        if num < min_num: min_num = num
        if num > max_num: max_num = num

    return min_num, max_num

# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([1.5, 2, 2.0, -3.1]))
# print(min_max([]))


#----------------------------------------------------------------------------------------------
#Сортировка


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных элементов."""
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result

# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

#----------------------------------------------------------------------------------------------
#Сплющ матрицы

def flatten(mat: list[list | tuple]) -> list:
    """Преобразует строки матрицы в один список."""
    if len(mat) == 0:
        raise ValueError('Пустая матрица')
    if all(isinstance(row, (list, tuple)) for row in mat):
        return [i for y in mat for i in y]
    else:
        raise TypeError("строка не строка строк матрицы")

# print(flatten([[1, 2], [3, 4]]))
# print(flatten([[1, 2], (3, 4, 5)]))
# print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], "ab"]))

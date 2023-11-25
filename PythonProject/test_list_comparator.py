import pytest
from ListComparator import ListComparator

@pytest.mark.parametrize("numbers, expected", [
    ([4, 3, 2, 1], 2.5),
    ([], 0),
    ([20, 30, 40], 30),
    ([-3, -2, -1], -2)
])
def test_average(numbers, expected):
    assert ListComparator.calculate_average(numbers) == expected

@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 1], [1, 2, 1], "Средние значения равны"),
    ([1, 2, 3, 4], [1], "Первый список имеет большее среднее значение"),
    ([1], [1, 2, 3, 4], "Второй список имеет большее среднее значение"),
    ([10, 20, 30], [1, 2, 3], "Первый список имеет большее среднее значение"),
    ([10, 20], [30, 40], "Второй список имеет большее среднее значение")
])
def test_compare_lists(list1, list2, expected):
    assert ListComparator.compare_lists(list1, list2) == expected
Отчет о выполнении задания:

Код программы:

class ListComparator:
    - Это класс для сравнения двух списков чисел.

    @staticmethod
    def calculate_average(numbers):  

        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

         - Вычисление среднего значения элементов списка.
         Параметр numbers - это список чисел для вычисления
         среднего. Метод возвращает 0 для пустого списка, либо
         среднее значение элементов списка.



    @staticmethod
    def compare_lists(list1, list2):
        
         - Сравнение средних значений двух списков, где list1 - это первый список чисел.
        list2 - это второй список чисел. Метод возвращает сообщение о сравнении средних значений списков.

        
        avg_list1 = ListComparator.calculate_average(list1)
        avg_list2 = ListComparator.calculate_average(list2)

        if avg_list1 > avg_list2:
            return "Первый список имеет большее среднее значение"
        elif avg_list1 < avg_list2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
           

Код тестов:


    import pytest
    from ListComparator import ListComparator

    1. Тестирование функции вычисления среднего значения списка.

    @pytest.mark.parametrize("numbers, expected", [
        ([4, 3, 2, 1], 2.5),
        ([], 0),
        ([20, 30, 40], 30),
        ([-3, -2, -1], -2)
    ])
    def test_average(numbers, expected):
        assert ListComparator.calculate_average(numbers) == expected

    2. Тестирование функции сравнения списков на основе их средних значений.
    

    @pytest.mark.parametrize("list1, list2, expected", [
        ([1, 2, 1], [1, 2, 1], "Средние значения равны"),
        ([1, 2, 3, 4], [1], "Первый список имеет большее среднее значение"),
        ([1], [1, 2, 3, 4], "Второй список имеет большее среднее значение"),
        ([10, 20, 30], [1, 2, 3], "Первый список имеет большее среднее значение"),
        ([10, 20], [30, 40], "Второй список имеет большее среднее значение")
    ])
    def test_compare_lists(list1, list2, expected):
    
        assert ListComparator.compare_lists(list1, list2) == expected


Отчет pylint/Checkstyle:
https://github.com/KseniaPaz/Unit-testsHW6/blob/main/PythonProject/info/Screenshot.png


Отчет о покрытии тестами:
https://github.com/KseniaPaz/Unit-testsHW6/blob/main/PythonProject/info/Screenshot1.png

Выбор сценариев:
Тестирование среднего значения - проверяет корректность расчета среднего значения, включая ситуацию с пустым списком.
Сравнение списков - покрывает три основных сценария: равные средние значения, первый список с большим средним значением и второй список с большим средним значением.
Эти сценарии выбраны, чтобы охватить основные возможности функций, учитывая граничные случаи и обеспечивая полное покрытие логических ветвей кода.
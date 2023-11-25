class ListComparator:

    @staticmethod
    def calculate_average(numbers):
        
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    @staticmethod
    def compare_lists(list1, list2):
       
        avg_list1 = ListComparator.calculate_average(list1)
        avg_list2 = ListComparator.calculate_average(list2)

        if avg_list1 > avg_list2:
            return "Первый список имеет большее среднее значение"
        elif avg_list1 < avg_list2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
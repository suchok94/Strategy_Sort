from strategies import IStrategy, BubbleSort, QuickSort, InsertSort

class Checker_strategy:

    @staticmethod
    def check(choosen_strategy):

        if choosen_strategy == 1:
            strategy = BubbleSort
        elif choosen_strategy == 2:
            strategy = QuickSort
        elif choosen_strategy == 3:
            strategy = InsertSort
        else:
            strategy = None

        return strategy

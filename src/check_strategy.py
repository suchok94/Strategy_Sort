from src.strategies import BubbleSort, QuickSort, InsertSort


class CheckerStrategy:

    @staticmethod
    def check(choice):

        if choice == "1":
            strategy = BubbleSort
        elif choice == "2":
            strategy = QuickSort
        elif choice == "3":
            strategy = InsertSort
        else:
            strategy = None

        return strategy

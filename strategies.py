from abc import ABC, abstractmethod


class IStrategy(ABC):

    @abstractmethod
    @staticmethod
    def sort(arr):
        pass


class BubbleSort(IStrategy):

    @staticmethod
    def sort(arr):
        length = len(arr)
        for i in range(0, length-1, 1):
            for j in range(i, length - i - 1, 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j + 1], arr[j]

        return arr

class QuickSort(IStrategy):
    @staticmethod
    def sort(self, arr):
        pass


class InsertSort(IStrategy):
    @staticmethod
    def sort(self, arr):
        pass


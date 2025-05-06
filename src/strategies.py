from abc import ABC, abstractmethod


class IStrategy(ABC):

    @staticmethod
    @abstractmethod
    def sort(arr):
        pass


class BubbleSort(IStrategy):

    @staticmethod
    def sort(arr):
        length = len(arr)
        for i in range(0, length-1, 1):
            for j in range(0, length - i - 1, 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j + 1], arr[j]

        return arr

class QuickSort(IStrategy):
    @staticmethod
    def sort(arr):
        less = []
        equal = []
        greater = []

        if len(arr) > 1:
            pivot = arr[0]
            for x in arr:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)

            return QuickSort(less) + equal + QuickSort(greater)

        else:
            return arr


class InsertSort(IStrategy):
    @staticmethod
    def sort(arr):
        length = len(arr)
        for i in range(0, length - 1, 1):
            imin = i  # index min
            for j in range(i + 1, length, 1):
                if arr[imin] < arr[j]:
                    imin = j
            arr[i], arr[imin] = arr[imin], arr[i]

        return arr


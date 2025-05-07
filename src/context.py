from src.strategies import IStrategy


class Context:

    def __init__(self, strategy= None):
        self.__strategy = strategy

    def set_strategy(self, strategy: IStrategy):
        self.__strategy = strategy

    def execute_strategy(self, list: list[int]):
        sorted_list = self.__strategy.sort(list)
        return sorted_list


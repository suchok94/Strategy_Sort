from gui import GUI
from context import Context
from check_strategy import Checker_strategy

class Application:

    def run(self):
        loop = True
        while loop == True:

            GUI.hello()
            сhoosen_strategy = GUI.get_data()
            strategy = Checker_strategy.check(сhoosen_strategy)
            context = Context()
            context.set_strategy(strategy)

            data = context.execute_strategy([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])
            GUI.result(data)
            loop = False
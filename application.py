from gui import GUI
from context import Context
from check_strategy import CheckerStrategy

class Application:

    def run(self):
        loop = True
        while loop == True:

            GUI.hello()
            choice = GUI.get_data()
            strategy = CheckerStrategy.check(choice)
            context = Context()
            context.set_strategy(strategy)
            GUI.get_arr()
            arr_numbers = []
            insert_arr = GUI.get_data()
            insert_arr = insert_arr.split(sep=',')
            arr_numbers.extend(insert_arr)
            data = context.execute_strategy(arr_numbers)
            GUI.result(data)
            loop = False
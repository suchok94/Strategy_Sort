from gui import GUI
from context import Context
from check_strategy import CheckerStrategy
from arrays import Arrays

class Application:

    def run(self):
        loop = True
        GUI.hello()
        while loop == True:
            GUI.choice_strategy_message()
            choice = GUI.get_data()
            strategy = CheckerStrategy.check(choice)
            if strategy != None:
                context = Context()
                context.set_strategy(strategy)
                GUI.get_arr()
                insert_arr = Arrays.str_to_int(Arrays.split(GUI.get_data()))
                data = context.execute_strategy(insert_arr)
                GUI.result(data)
                GUI.choice_different_strategy_message()

            else:
                GUI.incorrect_strategy()
                loop = False


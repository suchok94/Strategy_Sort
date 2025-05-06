class GUI:

    @staticmethod
    def hello():
        print(f'Это программа для сортировки чисел\n')


    @staticmethod
    def choice_strategy_message():
        print(f'Для выбора введите цифру:\n'
              f'\t"1" - пузырьком\n'
              f'\t"2" - быстрая\n'
              f'\t"3" - вставками')

    @staticmethod
    def get_data():
        data = input('Введите свой ответ: ')
        return data

    @staticmethod
    def result(data):
        print(f'получилось вот такое {data}')

    @staticmethod
    def get_arr():
        print('Введите массив ниже ')

    @staticmethod
    def incorrect_strategy():
        print('Вы выбрали неправильную стратегию.')

    @staticmethod
    def choice_different_strategy_message():
        print('\nВыберите другую стратегию')
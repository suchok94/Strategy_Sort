class GUI:

    @staticmethod
    def hello():
        print(f'Это программа для сортировки чисел\n'
              f'Выберите сортировку цифрами:'
              f'"1" - пузырьком'
              f'"2" - быстрая'
              f'"3" - вставками')

    @staticmethod
    def get_data():
        data = input('Введите свой ответ: ')
        return data

    @staticmethod
    def result(data):
        print(f'получилось вот такое {data}')

    @staticmethod
    def get_arr():
        print('Введите массив: ')
class GUI:

    @staticmethod
    def hello():
        print(f'Это программа для сортировки чисел\n'
              f'Выберите сортировку цифрами:')

    @staticmethod
    def get_data():
        data = int(input('Введите свой ответ: '))
        return data

    @staticmethod
    def result(data):
        print(f'получилось вот такое {data}')
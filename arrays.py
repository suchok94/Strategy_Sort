class Arrays:

    @staticmethod
    def split(string: str):
        if ',' in string or ', ' in string:
            arr = string.split(',')
        elif ';' in string or '; ' in string:
            arr = string.split(';')
        return arr

    @staticmethod
    def str_to_int(arr: list[str]):
        array_int = list(map(int, arr))
        return array_int

class Phone:
    def __init__(self, country, number):
        self.number = number
        self.country = country

    @staticmethod
    def get_code(code: str):
        codes = {
            'pl': 48,
            'de': 49,
            'ru': 7
        }

        return codes[code]

    def get_full_number(self):
        return self.get_code(self.country) + self.number


Phone.get_code('pl')

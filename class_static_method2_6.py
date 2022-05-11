class App:
    @staticmethod
    def main():
        print('hello world')

    @staticmethod
    def get_name():
        return 'Application'


if __name__ == '__main__':
    App.main()

    app = App
    print(app.get_name())

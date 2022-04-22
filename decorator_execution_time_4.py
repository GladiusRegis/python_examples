from time import sleep, time


def get_execution_details(function):
    def wrapper(*args, **kwargs):
        print('Ok, wrapper works.')
        print(*args),  # czas wyświetlony jako argument
        print(**kwargs)
        start = time()               # pobranie czasu przed startem
        output = function(*args, **kwargs)  # czas po starcie
        end = time()            # pobranie czasu po starcie
        print(f'Execution time {end - start}.')
        return output  # wynik czas przed i po starcie

    return wrapper


@get_execution_details
def go_to_sleep(time):
    sleep(time)
    print('test time')
    sleep(time)


go_to_sleep(3)

def main():
    while True:
        command = listen_command()
        do_command(command)


def listen_command():
    return input('Введите команду: ')


def do_command(command):
    message = command.lower()
    if message == 'привет':
        print('Привет!')
    elif message == 'пока':
        print('До новых встреч!')
        exit()
    else:
        print('Упс..\nНе понимаю :(')


if __name__ == '__main__':
    main()

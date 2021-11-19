from sys import argv, exit

num = int(argv[1])
new_value = argv[2]
with open('baker.csv', 'r+', encoding='utf-8') as f:
    if num != 1:
        i = 2
        line = f.readline()
        while i < num or not line:
            line = f.readline()
            i += 1
            if not line:
                print('Такой записи не существует')
                exit(1)
    pos = f.tell()  # OSError, если использовать for-in
    value = f.readline().strip()
    if len(value) == len(new_value):
        f.seek(pos)
        f.write(f'{new_value}\n')
    else:  # если новое значение длинней предыдущего - вариант короче не предусматривается
        rest = f.read()
        f.seek(pos)
        f.write(f'{new_value}\n')
        f.write(rest)

import sys

with open('data/users.csv', 'r', encoding='utf-8') as f1, \
        open('data/hobby.csv', 'r', encoding='utf-8') as f2, \
        open('users_hobby.txt', 'r', encoding='utf-8') as f3:
    for line1 in f1:
        line2 = f2.readline().strip()
        if not line2:
            line2 = None
        f3.write(f'{line1.strip()}: {line2}\n')
    content = f2.readline()
    if content:
        sys.exit(1)

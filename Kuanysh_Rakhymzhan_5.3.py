tutors = ['Иван', 'Анастасия', 'Игорь', 'Роберт', 'Сергей', 'Егор', 'Император']


klasses = ['11a', '10c', '9l', '7c', '1q', '777']

if len(tutors) > len(klasses):


    klasses += [None for i in range(len(tutors) - len(klasses))]

result = ((tutors[i], klasses[i]) for i in range(len(tutors)))


print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
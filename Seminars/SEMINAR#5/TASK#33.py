import random


def get_new_rating(rating, n, count=0, new_rating=None):
    if new_rating is None:
        new_rating = []
    if count == n:
        return new_rating
    else:
        new_rating.append(1) if rating[count] > 4 else new_rating.append(rating[count])
    return get_new_rating(rating, n, count + 1, new_rating)

n = int(input('Введите общее количество оценок: '))
rating = [random.randint(1, 5) for _ in range(n)]
print(rating)
print(get_new_rating(rating, n))
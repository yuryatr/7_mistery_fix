from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2

if __name__ == '__main__':
    starshiy, sredniy, svobodniy = map(int, input('Введите a, b, c: ').split())
    print('Корни уравнения: {0}, {1};'.format(*get_roots(starshiy, sredniy, svobodniy)))



# максимальное количество разбиений
MAX_CNT = 1_000_000

# метод левых прямоугольников
def leftRectsInt(func, a, b, k):
    step = (b - a) / k
    area = 0
    for ix in range(k):
        x = a + step * ix
        area += func(x) * step
    return area

# метод трапеции
def trapInt(func, a, b, k):
    step = (b - a) / k
    area = 0
    for ix in range(k):
        x = a + step * ix
        area += (func(x) + func(x+step)) * step / 2
    return area

# нахождение количества разбиений бин-поиском
def findSamplesCountEffective(integrate_method, func, a, b, eps):
    left = 1
    right = MAX_CNT

    while right - left > 1:
        mid = (right + left) // 2
        delta = abs(integrate_method(func, a, b, mid) - integrate_method(func, a, b, 2*mid))
        if delta > eps:
            left = mid
        else:
            right = mid
    return right

# нахождение количества разбиений перебором
def findSamplesCount(integrate_method, func, a, b, eps):
    for i in range(1, MAX_CNT):
        delta = abs(integrate_method(func, a, b, i) - integrate_method(func, a, b, 2*i))
        if delta < eps:
            return i
        
# вывод таблицы
def printTable(rows):
    columnSizes = [ max([len(str(x)) for x in el]) for el in zip(*rows) ]
    print('+' + '+'.join(['-' * (el+2) for el in columnSizes]) + '+')
    for row in rows:
        for i, el in enumerate(row):
            print(f"| {el:^{columnSizes[i]}} ", end="")
        print("|")
        print('+' + '+'.join(['-' * (el+2) for el in columnSizes]) + '+')
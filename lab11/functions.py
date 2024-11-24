import time

# вывод таблицы
def printTable(rows):
    columnSizes = [ max([len(str(x)) for x in el]) for el in zip(*rows) ]
    print('+' + '+'.join(['-' * (el+2) for el in columnSizes]) + '+')
    for row in rows:
        for i, el in enumerate(row):
            print(f"| {el:^{columnSizes[i]}} ", end="")
        print("|")
        print('+' + '+'.join(['-' * (el+2) for el in columnSizes]) + '+')

# получение времени выполнения функции
def getWithTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start
    return wrapper

# функция для создания кучи
def heaplify(arr, size, i, operations=0):
    largest = i
    next1, next2 = i*2+1, i*2+2

    if (next1 < size and arr[next1] > arr[largest]):
        largest = next1
    
    if (next2 < size and arr[next2] > arr[largest]):
        largest = next2
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        return heaplify(arr, size, largest, operations+1)
    
    return operations

# пирамидальная сортировка
def heapSort(arr):
    elements = len(arr)
    operations = 0

    for i in range(elements, -1, -1):
        heaplify(arr, elements, i, 0)
    
    for _ in range(elements):
        arr[elements-1], arr[0] = arr[0], arr[elements-1]
        elements -= 1
        operations += heaplify(arr, elements, 0)

    return arr, operations
EPS = 10e-5

def print_matrix(matrix, size_x, size_y, column_width):
    for y in range(size_y):
        for x in range(size_x):
            print(f"{matrix[y][x]:>{column_width}}", end=' ')
        print()

def scan_marix(el_type, size_x: int, size_y: int):
    matrix = []
    for _ in range(size_y):
        isEnter = True
        while isEnter:
            enter = list(map(el_type, input().split()))
            if len(enter) != size_x:
                print(f"В строке должно быть ровно {size_x} элементов!")
            else:
                isEnter = False

        matrix.append(enter)
    
    return matrix

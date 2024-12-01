import math

def encrypt_cardo_grid(text):
    # Удаление пробелов и перевод в нижний регистр
    clean_text = "".join(text.split()).lower()
    
    # Определение размера решетки
    length = len(clean_text)
    grid_size = math.ceil(math.sqrt(length))
    
    # Создание решетки
    grid = [[''] * grid_size for _ in range(grid_size)]
    
    # Заполнение решетки текстом
    for i in range(length):
        row = i // grid_size
        col = i % grid_size
        grid[row][col] = clean_text[i]
    
    # Создание шифра
    encrypted_text = ""
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j]:  # Только считываем заполненные ячейки
                encrypted_text += grid[i][j]
    
    return encrypted_text

# Пример использования
text = "Шифрование текстов с помощью решетки Кардано"
encrypted = encrypt_cardo_grid(text)
print("Зашифрованный текст:", encrypted)
nums = list(map(int, input("Введите элементы списка через пробел: ").split()))

first_honest, max_positive = -1, 0

for i in range(len(nums)):
    if first_honest == -1 and nums[i]%2 == 0:
        first_honest = i
    
    if nums[i] > nums[max_positive]:
        max_positive = i

if nums[max_positive] <= 0:
    print("Не найдено максимальное положительное чмсло")
elif first_honest == -1:
    print("Не найдено четное число")
else:
    nums[max_positive], nums[first_honest] = nums[first_honest], nums[max_positive]
    print("Измененный список: ", nums)
nums = list(map(int, input("Введите элементы списка через пробел: ").split()))

is_correct = False
while not is_correct:
    index = int(input("Введите индекс нового элемента: "))
    
    if 0 <= index < len(nums):
        is_correct = True
    else:
        print("Введите корректный индекс!")

for i in range(index, len(nums)-1):
    nums[i] = nums[i+1]

nums.pop()

print("Измененный список: ", nums)
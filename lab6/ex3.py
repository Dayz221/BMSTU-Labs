nums = list(map(int, input("Введите элементы списка через пробел: ").split()))

k = 0
isCorrect = False
while not isCorrect:
    k = int(input("Введите, какой экстремум необхожимо вывести: "))
    if k <= 0:
        print("Индекс экстремума должен быть больше 0!")
    else:
        isCorrect = True

cnt = 0
el = 0
for i in range(1, len(nums)-1):
    if (nums[i-1] < nums[i] > nums[i+1]) or (nums[i-1] > nums[i] < nums[i+1]):
        cnt += 1
        if cnt == k:
            el = nums[i]

if cnt < k:
    print("Экстремума с таким индексом нет в списке")
else:
    print(f"{k} экстремум: {el}")
nums = list(map(int, input("Введите элементы списка через пробел: ").split()))

curAnsw = [nums[0]]
maxLenArr = []

for i in range(0, len(nums)-1):
    cur, next = nums[i], nums[i+1]
    if ((cur >= 0 and next < 0) or (cur < 0 and next >= 0)) and cur%2 == 1 and next%2 == 1:
        curAnsw.append(next)
    else:
        if len(curAnsw) > len(maxLenArr):
            maxLenArr = curAnsw.copy()
        curAnsw = [next]

if len(curAnsw) > len(maxLenArr):
    maxLenArr = curAnsw.copy()

if len(maxLenArr) < 2:
    print("Такой последовательности нет")
else:
    print("Ответ: ", maxLenArr)
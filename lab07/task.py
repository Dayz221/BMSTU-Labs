str_num = input()
k = int(input())

if k >= len(str_num):
    print(0)
    
else:
    num = []
    for i in str_num:
        i = int(i)

        while len(num) > 0 and k > 0 and num[-1] > i:
            num.pop()
            k -= 1
        
        if len(num) != 1 or i != 0: num.append(i)

    while len(num) > 1 and k > 0:
        num.pop()
        k -= 1

    print(int(''.join([str(i) for i in num])))
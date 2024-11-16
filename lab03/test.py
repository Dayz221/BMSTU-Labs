m, n = map(int, input().split())
t = min(m, n)

while t > 0:
    if m%t == 0:
        if n%t == 0:
            print(t)
            break
    t -= 1
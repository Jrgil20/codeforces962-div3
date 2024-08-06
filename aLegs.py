def Animals(legs):
    if legs % 2 != 0:
        return 0
    elif legs % 4 == 0:
        return legs // 4
    else:
        return legs// 4 + 1


n = int(input())

for _ in range(n):
    num = int(input())
    print(Animals(num))
 

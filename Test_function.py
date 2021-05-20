from Generate import check

a = [14, 7]
b = [0, 7]
c = [14, 8]
print(check(a, b, c, 14))
if 0 in b or 14 in b:
    if (a[0] in range(2, 12) or a[1] in range(2, 12) and a[0] != 14 and a[0] != 0 and a[1] != 14 and a[1] != 0)\
            or (c[0] in range(2, 12) or c[1] in range(2, 12) and c[0] != 14 and c[0] != 0 and c[1] != 14 and c[1] != 0):
        print(False)

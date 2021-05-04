def xline(a, b):
    lst = []
    match = []
    # Case 1
    for i in range(1, 5):
        if a[1] + i <= 14:
            lst.append([a[0], a[1] + i])
        if a[1] - i >= 0:
            lst.append([a[0], a[1] - i])
        if a[0] + i <= 14:
            lst.append([a[0] + i, a[1]])
        if a[0] - i >= 0:
            lst.append([a[0] - i, a[1]])
        if a[0] + i <= 14 and a[1] + i <= 14:
            lst.append([a[0] + i, a[1] + i])
        if a[0] - i >= 0 and a[1] - i >= 0:
            lst.append([a[0] - i, a[1] - i])
        if a[0] - i >= 0 and a[1] + i <= 14:
            lst.append([a[0] - i, a[1] + i])
        if a[0] + i <= 14 and a[1] - i >= 0:
            lst.append([a[0] + i, a[1] - i])
    for i in range(1, 5):
        if b[1] + i <= 14:
            if [b[0], b[1] + i] in lst:
                match.append([b[0], b[1] + i])
        if b[1] - i >= 0:
            if [b[0], b[1] - i] in lst:
                match.append([b[0], b[1] - i])
        if b[0] + i <= 14:
            if [b[0] + i, b[1]] in lst:
                match.append([b[0] + i, b[1]])
        if b[0] - i >= 0:
            if [b[0] - i, b[1]] in lst:
                match.append([b[0] - i, b[1]])
        if b[0] + i <= 14 and b[1] + i <= 14:
            if [b[0] + i, b[1] + i] in lst:
                match.append([b[0] + i, b[1] + i])
        if b[0] - i >= 0 and b[1] - i >= 0:
            if [b[0] - i, b[1] - i] in lst:
                match.append([b[0] - i, b[1] - i])
        if b[0] - i >= 0 and b[1] + i <= 14:
            if [b[0] - i, b[1] + i] in lst:
                match.append([b[0] - i, b[1] + i])
        if b[0] + i <= 14 and b[1] - i >= 0:
            if [b[0] + i, b[1] - i] in lst:
                match.append([b[0] + i, b[1] - i])
    # Filter
    if a[0] == b[0]:
        i = 0
        while i <= len(match) - 1:
            if match[i][0] == min(a, b)[0] and abs(match[i][1] - min(a, b)[1]) <= 5:
                match.pop(i)
            else:
                i += 1
    elif a[1] == b[1]:
        i = 0
        while i <= len(match) - 1:
            if match[i][1] == min(a, b)[1] and abs(match[i][0] - min(a, b)[0]) <= 5:
                match.pop(i)
            else:
                i += 1
    i = 0
    while i <= len(match) - 1:
        if abs(match[i][0] - a[0]) + 1 == 5 or abs(match[i][1] - a[1]) + 1 == 5:
            match.remove(match[i])
        elif abs(match[i][0] - b[0]) + 1 == 5 or abs(match[i][1] - b[1]) + 1 == 5:
            match.remove(match[i])
        else:
            i += 1
    return match


def check(a, b, c, n):
    # a and c is black stone
    # b is white stone.
    # n is size of board
    chk = xline(a, c)
    # Filter
    # 1. Ignore close stone
    # 1.1 Check a, b
    t1 = True
    if abs(a[0] - b[0]) + 1 < 4 or abs(a[1] - b[1]) + 1 < 4:
        t1 = False - 1
    t2 = True
    if abs(b[0] - c[0]) + 1 < 4 or abs(b[1] - c[1]) + 1 < 4:
        t2 = False - 1
    t3 = True
    if abs(a[0] - c[0]) + 1 <= 3 or abs(a[1] - c[1]) + 1 <= 3:
        t3 = False
    if t1 + t2 + t3 < 2:
        return False
    if chk:
        chk.append(a)
        chk.append(c)
        for i in chk:
            if i[1] == 0:
                continue
            # Solve
            if abs(i[0] - b[0]) + 1 <= 6:
                return True
        if len(chk) == 4:
            if a[0] == c[0] == 0 or a[1] == c[1] == 0 or a[0] == c[0] == n or a[1] == c[1] == n:
                if b[0] == 0 or b[1] == 0 or b[0] == n or b[1] == n:
                    if abs(a[1] - c[1]) + 1 <= 4 or abs(a[0] - c[0]) + 1 <= 4:
                        return True
    else:
        if b[0] == 0 or b[1] == 0 or b[0] == n or b[1] == n:
            # if abs(a[0] - b[0])
            return True
        return False


def generate(n):
    f = open('Output.txt', 'w')
    arr = []
    for y in range(0, n + 1):
        for x in range(0, n + 1):
            for y1 in range(0, n + 1):
                for x1 in range(0, n + 1):
                    for y2 in range(0, n + 1):
                        for x2 in range(0, n + 1):
                            if [x, y] != [x1, y1] != [x2, y2] and [x1, y1] != [x2, y2] != [x, y] \
                                    and [x2, y2] != [x, y] != [x1, y1]:
                                if check([x, y], [x1, y1], [x2, y2], n):
                                    f.write('{}, {} - {}, {} - {}, {}\n'.format(x, y, x1, y1, x2, y2))
                                    arr.append([[x, y], [x1, y1], [x2, y2]])
    f.close()
    print('Possible opening:', len(arr))


print(generate(14))
# print(check([3, 9], [14, 14], [14, 0], 14))

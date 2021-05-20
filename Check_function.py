def xline(a, b):
    print('START')
    if abs(a[0] - b[0]) + 1 >= 7 or abs(a[1] - b[1]) + 1 >= 7:
        return []
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
    print('Match:', match)
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
    print('A, C:', a, c)
    print('Check match:', chk)
    # Filter
    # 1. Ignore bad opening
    if 0 in b or 14 in b:
        if a[0] in range(2, 12) or a[1] in range(2, 12) or b[0] in range(2, 12) or b[1] in range(2, 12):
            return False
    # 2. Ignore close stone
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
        print('Check')
        for i in chk:
            if i[1] == 0 or i[0] == 0:
                continue
            # Solve
            if i == a or i == c:
                print('\t+ i == a or i == c:')
                if abs(i[0] - b[0]) + 1 <= 5 and abs(i[1] - b[1]) + 1 <= 5:
                    return True
            print('\t+ {} - {}:'.format(i, b))
            if abs(i[0] - b[0]) + 1 <= 6 and abs(i[1] - b[1]) + 1 <= 6:
                print('\t\t+ Check X:', abs(i[0] - b[0]) + 1)
                print('\t\t+ Check Y:', abs(i[1] - b[1]) + 1)
                return True
        print('Len 4 Check:')
        if len(chk) == 4:
            if a[0] == c[0] == 0 or a[1] == c[1] == 0 or a[0] == c[0] == n or a[1] == c[1] == n:
                if b[0] == 0 or b[1] == 0 or b[0] == n or b[1] == n:
                    if abs(a[1] - c[1]) + 1 <= 4 or abs(a[0] - c[0]) + 1 <= 4:
                        return True
    else:
        print('Else check:')
        if b[0] == 0 or b[1] == 0 or b[0] == n or b[1] == n:
            return True
        return False


print(check([10, 7], [13, 13], [7, 7], 14))

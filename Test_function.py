def xline(a, b):
    x1, y1 = a
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
        print('Min:', min(a, b))
        while i <= len(match)-1:
            print('Current:', match[i])
            if match[i][0] == min(a,b)[0] and abs(match[i][1] - min(a,b)[1]) <= 5:
                print('--> Deleted')
                match.pop(i)
            else:
                i += 1
    elif a[1] == b[1]:
        i = 0
        while i <= len(match)-1:
            print('Current:', match[i])
            if match[i][1] == min(a, b)[1] and abs(match[i][0] - min(a, b)[0]) <= 5:
                print('--> Deleted')
                match.pop(i)
            else:
                i += 1

    return match


inp1 = (7, 2)
inp2 = (12, 4)
print(xline(inp1, inp2))

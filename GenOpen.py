from connect import *


def generate():
    pass


def evaluate():
    pass


def xline(a, b):
    x1, y1 = a
    lst = [[x1, y1]]
    match = []
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
    if a[0] == b[0]:
        i = 1
        while [min(a, b)[0], min(a, b)[1] + i] in match:
            match.remove([min(a, b)[0], min(a, b)[1] + i])
            i += 1
    elif a[1] == b[1]:
        i = 1
        while [min(a, b)[0]+i, min(a, b)[1]] in match:
            match.remove([min(a, b)[0]+i, min(a, b)[1]])
            i += 1
    return match


def distance():
    pass

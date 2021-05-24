def remove_duplicate(fn):
    f = open(fn, 'r')
    wr = open('Gen_RD.txt', 'w')
    data = f.read().split('\n')
    data = [i.split(' - ') for i in data]
    data.pop(len(data)-1)
    print('Total lines:', len(data))
    for i in data:        
        if data.index(i) == line:
            print('Line:', data.index(i))
            line += 10000
        a = i[0]
        b = i[1]
        c = i[2]
        
        if [c, b, a] in data:
            data.remove([c, b, a])
        wr.write(a + ' - ' + b + ' - ' + c + '\n')

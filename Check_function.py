import threading


class WorkerThread(threading.Thread):
    def __init__(self, data, maxi):
        super().__init__()
        self.data = data    # Initialize data for thread
        self.max = maxi

    def run(self):
        # This method is invoked when starting a thread
        # Do the work of thread here.
        pass


def remove_duplicate(fn):
    f = open(fn, 'r')
    wr = open('Gen_RD.txt', 'a+')
    data = f.read().split('\n')
    data = [i.split(' - ') for i in data]
    data.pop(len(data)-1)
    #Extend
    lst = data[180230:]
    print('Lines:', len(data))
    print('STEP 1: FILTER')
    line = 0
    k = 0
    for i in lst:        
        if data.index(i) == line:
            print('Line:', data.index(i))
            line += 10000
        elif data.index(i) > line and k == 0:
            line = data.index(i) // line * line
            print('Line:', line)
            k = 1
        a = i[0]
        b = i[1]
        c = i[2]
        
        if [c, b, a] in data:
            data.remove([c, b, a])
        wr.write(a + ' - ' + b + ' - ' + c + '\n')
        


remove_duplicate('Generate\\Gen.txt')

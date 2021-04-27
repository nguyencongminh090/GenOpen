import subprocess


def __init__(engines):
    global engine
    engine = subprocess.Popen(engines, universal_newlines=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)


def send(command):
    engine.stdin.write(command + '\n')


def get_info():
    """
    :return: Evaluate
    """
    while True:
        try:
            text = engine.stdout.readline().strip()
            if 'MESSAGE' in text and 'depth' in text:
                sp = text.split(' ')
                depth = sp[sp.index('depth')+1]
                ev = sp[sp.index('ev')+1]
                engine.stdout.readline().strip()
                return ev
        except:
            pass

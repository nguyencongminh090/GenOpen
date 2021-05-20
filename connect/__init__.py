import subprocess
import time
import keyboard


def init(engines):
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
            if keyboard.is_pressed('esc'):
                print('Hotkey pressed')
                break
            text = engine.stdout.readline().strip()
            if 'MESSAGE' in text and 'depth' in text:
                sp = text.split(' ')
                ev = sp[sp.index('ev')+1]
                text = engine.stdout.readline().strip()
                if 'MESSAGE' not in text:
                    return ev
                sp = text.split(' ')
                ev = sp[sp.index('ev') + 1]
                return ev
        except:
            pass


def config(times, ram_limit):
    """
    :param times: Time in seconds.
    :param ram_limit: Ram Limit in GB.
    """
    try:
        times = str(int(times) * 1000)
        send('START 15')
        send('INFO max_memory {}'.format(1024**3*ram_limit))
        send('INFO timeout_match ' + times)
        send('INFO timeout_turn ' + times)
        send('INFO game_type 1')
        send('INFO rule 1')
        send('INFO time_left ' + times)
    except:
        times = str(int(times) * 1000)
        send('START 15')
        send('INFO max_memory {}'.format(1024 ** 3 * ram_limit))
        send('INFO timeout_match ' + times)
        send('INFO timeout_turn ' + times)
        send('INFO game_type 1')
        send('INFO rule 1')
        send('INFO time_left ' + times)


def test_sw(opening, times, ram_limit):
    config(times, ram_limit)
    send('BOARD')
    for i in range(len(opening)):
        if len(opening) % 2 == i % 2:
            send(opening[i] + ',' + '1')
        else:
            send(opening[i] + ',' + '2')
        time.sleep(0.5)
    send('DONE')
    output = get_info()
    send('RESTART')
    return output


def exit_engine():
    send('END')
    engine.kill()

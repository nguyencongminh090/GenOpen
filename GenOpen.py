from connect import *
from Gen import generate
from remove_duplicate import remove_duplicate
import json
import os


def evaluate(time_set, ram_limits=2):
    t = open('Generate\\Gen.txt', 'r')    
    data = t.read().split('\n')
    data = data[:-1]
    t.close()
    
    for i in range(len(data)):
        # Filter        
        print('ID:', i)
        opening = data[i].split(' - ')
        evaluates = float(test_sw(opening, time_set, ram_limits))
        if 30 <= evaluates <= 80:
            write_output = open('Evaluate\\Final.txt', 'a+')
            write_output.write('\n{} - [{}]'.format(data[i], evaluates))            
            print('ID:', i, '//', data[i])
            print('{} - [{}]'.format(data[i], evaluates))
            write_output.close()


f = open('config.json')
config = json.load(f)
board_size = config['board-size']

while True:
    os.system('cls')
    print('What do you want?')
    print('[1] Generate opening (default)')
    print('[2] Evaluate opening')
    print('[3] About')
    print('[4] Exit')
    inp = int(input('Choice: '))
    if inp == 4:
        exit()
    elif inp == 3:
        os.system('cls')
        print('ABOUT ME AND MY PROJECT:')
        print("- My name Nguyen Cong Minh. I'm 15 years old. My project is about generate opening for Gomoku.")
        print('NOTE: This project still in develop, if you found some bug you can send email to me.')
        print('EMAIL: nguyencongminh050@gmail.com')
        print('Github: nguyencongminh090')
        print('\n\n(Press enter to continue)')
        os.system('pause>nul')
        continue
    elif inp == 2:
        os.system('cls')
        init('Engine\\engine.exe')
        print('EVALUATE')
        print('------------')
        times = input('Time (seconds): ')
        print('Default value for Ram Limit is 2 GB')
        ram_limit = int(input('Ram Limit (GB): '))
        evaluate(times, ram_limit)
        print('Status: DONE')
##        os.system('pause>nul')
        exit_engine()
        os.system('shutdown -s -t 00')
    elif inp == 1:
        os.system('cls')
        print('GENERATE')
        print('------------')
        generate(board_size)
        print('REMOVE DUPLICATE')
        remove_duplicate('Generate\\Gen.txt')
        print('Status: DONE')
        os.system('pause>nul')

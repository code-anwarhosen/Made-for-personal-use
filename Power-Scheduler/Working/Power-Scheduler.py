import os
import time
from wakepy import keepawake, unset_keepawake
from datetime import datetime, timedelta

def schedule_shutdown(hours):
    target = datetime.now() + timedelta(hours=float(hours))
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\nYour computer will shutdown after {hours} hour!\n')

    while datetime.now() < target:
        print('Time left : ', target - datetime.now())
        time.sleep(60)
        
    if datetime.now() >= target:
        print('\n####### Press "Ctrl + C" to cancel #######\n')
        i = 10
        while i > 0:
            print(f'power-Off in {i} seconds')
            i -= 1
            time.sleep(1)
            os.system('cls')
        print('power off')
        unset_keepawake()
        os.system("shutdown /s /f /t 1")

print('###### Power-Off Scheduler ###### \n\n# Enter 0 to shutdown immediately')
print('# Enter 0.1=6 minutes, 1=1 hour. \n')

hours = ''
while not type(hours) == float:
    hours = input('Shutdown after ?? hours?: ')
    try:
        hours = float(hours)
    except Exception as e:
        print('Enter a number.')

with keepawake(keep_screen_awake=False):
    schedule_shutdown(hours)

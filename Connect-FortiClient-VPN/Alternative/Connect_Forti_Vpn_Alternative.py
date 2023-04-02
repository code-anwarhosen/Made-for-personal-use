import os
import time
import socket
import pyautogui
import subprocess
import pygetwindow
from pathlib import Path

try:
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, r'credentials.txt')
    if os.path.exists(dirname):
        with open(file_path, 'r') as file:
            text = file.readlines()
    password, filename = text[0], text[1]

    PASSWORD = password.split()[0]
    SCRIPT_WIN = filename.split()[0]
except Exception as e:
    print(e)
    PASSWORD = 'VPN@#mand12'
    SCRIPT_WIN = 'FortiPass'


VPN_WIN = 'FortiClient'
LOCAL_IP = '172.16.130.82'

FORTI_VPN = "C:/Program Files/Fortinet/FortiClient/FortiClient.exe"

# Check if a given exe applicatis is open
def is_open(application):
    target = ('tasklist', '/fi', f'imagename eq {application}')
    output = subprocess.check_output(target).decode()
    app_name = output.strip().split('\r\n')[-1]
    return app_name.lower().startswith(application.lower())

def has_internet():
    ip_address = socket.gethostbyname(socket.gethostname())
    if ip_address == '127.0.0.1':
        print('\nNo internet access\n')
        return False
    else:
        return True

def is_vpn_connected(local_ip):
    current_ip = socket.gethostbyname(socket.gethostname())
    if current_ip == '10.5.4.23':
        return True
    else:
        return False

def activate_vpn_window():
    try:
        vpn_window = pygetwindow.getWindowsWithTitle(VPN_WIN)[0]
        vpn_window.activate()
    except Exception as e:
        print('Error : ', e)
def resize_window():
    # resize and move the python window 
    try:
        py_window = pygetwindow.getWindowsWithTitle(SCRIPT_WIN)[0]
        py_window.resizeTo(200, 500)
        py_window.moveTo(-8, 0)
        # py_window.minimize()
    except Exception as e:
        print('Error : ', e)
    activate_vpn_window()

def connect_vpn(password):
    if is_open('forticlient.exe'):
        print('VPN Opened!\n')
        activate_vpn_window()

        pyautogui.press('tab', presses=3)
        pyautogui.write(password, interval=0.10)
        time.sleep(2)
        pyautogui.press('enter')

        for i in range(0, 10):
            print('Connecting to VPN!')
            if is_vpn_connected(LOCAL_IP):
                print('\nVPN connected!')
                print('\tQuiting!')
                time.sleep(5)
                py_window = pygetwindow.getWindowsWithTitle(SCRIPT_WIN)[0]
                py_window.close()
            has_internet()
            time.sleep(10)
    else:
        print('VPN is not open!')


#++++++++++++++++++++++++++ Entry Point +++++++++++++++++++++#
if is_vpn_connected(LOCAL_IP):
    print('VPN is already connected!\n')
    action = str(input('Enter D to disconnect \nPress Enter to Quit : ')).lower()
    if action == 'd':
        try:
            subprocess.Popen(FORTI_VPN)
            time.sleep(5)
            activate_vpn_window()
            pyautogui.press('tab')
            pyautogui.press('enter')

            py_window = pygetwindow.getWindowsWithTitle(SCRIPT_WIN)[0]
            py_window.close()
        except Exception as e:
            print('Error : ', e)
    else:
        print('\tQuiting!')
        time.sleep(2)
else:  
    try:
        if has_internet():
            subprocess.Popen(FORTI_VPN)
            time.sleep(5)
            resize_window()

            for i in range(0, 3):
                if has_internet():
                    connect_vpn(PASSWORD)
                time.sleep(3)
        else:
            print('\tQuiting!')
            time.sleep(5)
            py_window = pygetwindow.getWindowsWithTitle(SCRIPT_WIN)[0]
            py_window.close()

    except Exception as e:
        print(e)
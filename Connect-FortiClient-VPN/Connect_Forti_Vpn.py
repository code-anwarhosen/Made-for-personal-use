import os
import time
import pyautogui
import subprocess
import pygetwindow
from PIL import Image
from pytesseract import pytesseract


img_path = "Files/Screenshot.png"
txt_file = 'Files/Screenshot-Text.txt'
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
forti_app_path = r"C:\Program Files\Fortinet\FortiClient\FortiClient.exe"
pytesseract.tesseract_cmd = path_to_tesseract

def activate_vpn_window():
    # activate the vpn window 
    try:
        vpn_window = pygetwindow.getWindowsWithTitle('FortiClient')[0]
        vpn_window.activate()
    except Exception as e:
        pass

def resize_window():
    # resize and move the python window 
    try:
        py_window = pygetwindow.getWindowsWithTitle('FortiPass')[0]
        py_window.resizeTo(200, 700)
        py_window.moveTo(-8, 0)
        # py_window.minimize()
    except Exception as e:
        pass
    activate_vpn_window()

def delete_screenshot(img_path):
    try:
        with open(img_path) as file:
            if file:
                file.close()
                os.remove(img_path)
                # print('Image Deleted')
    except Exception as e:
        print('File deletion Error: ', e)

def take_screenshot():
    if not os.path.exists(os.path.dirname(img_path)):
        try:
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
        except Exception as e:
            print('File Error: ', e)
    img = pyautogui.screenshot(img_path)

def read_screenshot():
    img = Image.open(img_path)
    
    try:
        text = pytesseract.image_to_string(img)
        if type(text) is str:
            text = text.lower()
    except Exception as e:
        pass
    
    if not os.path.exists(os.path.dirname(txt_file)):
        try:
            os.makedirs(os.path.dirname(txt_file), exist_ok=True)
        except Exception as e:
            print('File Error: ', e)
    with open(txt_file, 'w') as file:
        file.write(text)
        file.close()

    helpText = 'upgrade to the full version to access additional features and receive technical support'
    if (
            ('forticlient' and 'singer-vpn' in text) or
            ('forticlient' and 'file help' in text) or
            ('file help' and helpText in text) or
            ('singer-vpn' and helpText in text) or
            ('singer-vpn' and 'file help' in text)
        ):
        print('VPN opened!')
        activate_vpn_window()
        
        pyautogui.press('tab', presses=3)
        pyautogui.write('mand@#VPN12', interval=0.10)
        time.sleep(2)
        pyautogui.press('enter')

        time.sleep(60)
        py_window = pygetwindow.getWindowsWithTitle('FortiPass')[0]
        py_window.close()

        return 'end'
    elif 'vpn connected' in text:
        print('vpn connected')
        return 'end'
    else:
        print('VPN is not opened!')

try:
    subprocess.Popen(forti_app_path)
except:
    pass
time.sleep(2)
resize_window()
for i in range(0, 10):
    delete_screenshot(img_path)
    take_screenshot()
    end = read_screenshot()
    if end == 'end':
        break
    time.sleep(3)

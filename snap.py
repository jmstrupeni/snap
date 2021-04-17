import pyautogui, os, time, pyperclip

p = pyautogui
cwd = os.path.dirname(__file__)
time.sleep(5)
screenshot = p.screenshot()
filename = p.prompt(text='Enter file name.',title='snap.py')
screenshot.save(os.path.join(cwd,filename)+'.jpg')
pyperclip.copy(cwd)

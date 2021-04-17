import pyautogui, os, time, pyperclip, argparse

parser = argparse.ArgumentParser(
    description = 'Script to take a snapshot, ask for a file name, save it and copy destination path to clipboard.')
parser.add_argument('-e', help='When given, open file explorer in file destination path.', action='store_true')
args = parser.parse_args()

p = pyautogui
cwd = os.path.dirname(__file__)
time.sleep(5)
screenshot = p.screenshot()
filename = p.prompt(text='Enter file name.',title='snap.py')
screenshot.save(os.path.join(cwd,filename)+'.jpg')
pyperclip.copy(cwd)

if args.e:
    os.startfile(cwd)

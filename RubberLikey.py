import time
import argparse
from pynput.keyboard import Controller, Key
import sys

keyboard = Controller()

def parse_ducky_line(line, realistic=False):
    if line.startswith("DELAY"):
        delay = int(line.split()[1])
        time.sleep(delay / 1000)
    elif line.startswith("STRING"):
        text = line[len("STRING "):]
        if realistic:
            for char in text:
                keyboard.type(char)
                time.sleep(0.03)  # 30ms per character
        else:
            keyboard.type(text)
    elif line.startswith("ENTER"):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif line.startswith("TAB"):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    elif line.startswith("GUI"):
        keyboard.press(Key.cmd)
        time.sleep(0.1)
        keyboard.release(Key.cmd)
    elif line.startswith("SHIFT"):
        key = line.split()[1]
        keyboard.press(Key.shift)
        keyboard.press(key)
        keyboard.release(key)
        keyboard.release(Key.shift)
    else:
        print(f"[!] Unknown or unsupported command: {line.strip()}")

def run_ducky_script(path, realistic=False):
    print(f"[+] Running DuckyScript from: {path}")
    print(f"[i] Realistic delays: {'ON' if realistic else 'OFF'}")
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("REM"):
                continue
            print(f"[*] {line}")
            parse_ducky_line(line, realistic=realistic)
            if realistic:
                time.sleep(0.1)  # 100ms between commands
            else:
                time.sleep(0.15)  # 150ms by default to avoid crashes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate DuckyScript payloads locally.")
    parser.add_argument("payload", help="Path to DuckyScript payload.txt")
    parser.add_argument("--realistic", action="store_true", help="Enable realistic typing and delays")

    args = parser.parse_args()
    run_ducky_script(args.payload, realistic=args.realistic)

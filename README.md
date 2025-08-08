# 🦆 RubberLikey

**Test your USB Rubber Ducky payloads – no hardware required.**  
`RubberLikey.py` is a cross-platform Python tool that emulates DuckyScript payloads locally, letting you debug and refine `payload.txt` files before flashing the real device.

---

## 🚀 Features

- 🖥 **Local execution** – run your payloads on Windows, Linux, or macOS.
- ⌨️ Supports core DuckyScript commands:
  - `DELAY`
  - `STRING`
  - `ENTER`
  - `TAB`
  - `GUI`
  - `SHIFT <key>`  
- ⚡ **Realistic mode** (`--realistic`) – adds human-like typing & pacing.
- 🛡 **Safe default delays** – prevents GUI/app crashes while testing.
- 🔍 Console logs every executed command.

---

## 📦 Installation

```bash
git clone https://github.com/Sec-Llama/RubberLikey.git
cd RubberLikey
pip install pynput
```

---

## 🛠 Usage

### Basic run
```bash
python RubberLikey.py payload.txt
```

### Realistic typing & pacing
```bash
python RubberLikey.py payload.txt --realistic
```

---

## 📁 Example `payload.txt`
```text
REM Open Run dialog
GUI r
DELAY 300
STRING notepad
ENTER
DELAY 500
STRING Hello from RubberLikey!
ENTER
```

---

## 🎯 Roadmap

- [ ] Keyboard layout mapping (`en-us`, `es-la`, etc.)
- [ ] Clipboard injection (CTRL+V)
- [ ] GUI interface
- [ ] Dry-run preview mode
- [ ] Log output to file

---

## ⚠️ Disclaimer
This tool is for **educational and authorized security testing only**.  
The author is not responsible for any misuse.

---

💀 *Hack smart. Test safe.*

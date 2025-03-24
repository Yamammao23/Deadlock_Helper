Description, how to run

# Deadlock Helper

Deadlock Helper is a companion application for the game **Deadlock** that helps you analyze the enemy team and suggests optimal gear choices. It works by detecting characters displayed in the top bar of the game screen and providing gear recommendations based on their matchups.

This is a modular, Python-based project designed for future expansion — including screen capture, image recognition, and an optional in-game overlay.

---

## 🚀 Features (planned)
- Detect characters from Deadlock's top bar
- Recommend gear based on matchups
- Display a helper window on your secondary monitor
- Optional in-game transparent overlay for quick reference

---

## 🧰 How to Run

### 1. Clone the project

```bash
git clone https://github.com/your-username/deadlock-helper.git
cd deadlock-helper
```

2. Create a virtual environment

```bash
python -m venv venv

source venv/bin/activate        # On macOS/Linux

venv\Scripts\activate           # On Windows
```

3. Install dependencies

```bash
pip install -r Deadlock_overlay\\requirements.txt
```

4. Run the app

```bash
python  Deadlock_overlay\\run.py
```

The helper window will open on your secondary monitor by default. This window will eventually be used to display character matchups and gear suggestions.


🛠 Tech Stack

Python 3.10+

PySimpleGUI — for UI

screeninfo — to detect and position on multiple monitors

(Planned) opencv-python and pillow for image recognition

📁 Project Structure
```bash
deadlock_helper/
├── deadlock_helper/      # Core logic
│   ├── ui.py             # GUI window logic
│   ├── screen.py         # Monitor detection
│   └── ...
├── run.py                # App entry point
├── requirements.txt
└── README.md
```

🧪 Development Status

This is an early-stage prototype. Expect active development and breaking changes. Contributions, suggestions, and ideas are welcome!

---

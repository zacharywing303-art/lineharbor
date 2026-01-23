🏁 DSLR Race Timer PRO
🎥 Computer‑Vision Photo Finish System for School Athletics
A Python + OpenCV based live race timing system that uses a DSLR / webcam to automatically detect when athletes cross the finish line and records accurate timestamps per lane.

Built for:

🏫 School sports day

🏃 Track races (100m, 200m, etc.)

📸 Low‑cost photo finish replacement

💻 Windows laptops

✨ Features
✅ Live DSLR / webcam feed
✅ Fullscreen professional UI
✅ Draw lane lines with mouse
✅ Draw finish line segments
✅ Automatic finish detection
✅ Per‑lane timestamps
✅ Big digital race timer
✅ Motion / AI based tracking
✅ Slow‑motion replay
✅ Results panel
✅ Watermark credit (@akulsaju)
✅ Exportable (can build .exe app)

📸 How it Works
Camera points at finish line (side view)

Draw lanes and finish line

Start race

When athlete crosses → motion detected

Time recorded automatically

Lane 1 → 11.23s
Lane 3 → 11.41s
Lane 2 → 11.44s
🖥 Requirements
Hardware
DSLR or Webcam

Tripod (stable camera)

HDMI capture card (recommended for best quality)

Software
Windows 10/11

Python 3.11+ (recommended)

OpenCV

NumPy

⚙ Installation
1. Install Python
Download:
👉 https://python.org

2. Install dependencies
Open CMD or PowerShell:

py -m pip install opencv-python numpy
3. Run program
python race_timer.py
🚀 Build as Windows App (.exe)
No terminal needed. Double‑click app.

Install PyInstaller
py -m pip install pyinstaller
Build
py -m PyInstaller --onefile --noconsole race_timer.py
Output
dist/race_timer.exe
Run like normal software.

🎮 Controls
Key	Action
L	Draw lanes
F	Draw finish lines
S	Start race
R	Slow motion replay
Q	Quit
Mouse:

Click + drag → draw line

📷 Camera Setup Tips (IMPORTANT)
For best accuracy:

✅ 1080p or higher
✅ 60 FPS or higher
✅ Side view of finish line
✅ Fixed tripod
✅ HDMI capture (avoid webcam compression)

Example:

Camera  →  Finish line (side angle)
NOT front view.

🧠 Detection Method
Uses:

Frame differencing

Motion detection

Masked finish line crossing

Per‑lane timestamp logging

No ML required → fast + runs on any laptop.

📂 Project Structure
race_timer.py
README.md
dist/ (after build)
🔮 Future Improvements (ideas)
GUI buttons (Start/Stop)

CSV export

Auto lane detection

Photo finish zoom window

Athlete tracking with AI

Scoreboard overlay

Touchscreen support

Multi‑camera support

👨‍💻 Author
Built by
@akulsaju


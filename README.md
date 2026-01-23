# 🏃 DSLR Race Timer (Finish Line Auto Detection)

A Python + OpenCV based **school athletics race timer** that uses a DSLR (or webcam) to automatically detect when athletes cross the finish line and logs:

✅ Lane number  
✅ Finish time  
✅ Order (1st, 2nd, 3rd…)  
✅ Live video overlay  
✅ Works in real‑time  
✅ Windows compatible  
✅ Can export as .exe app  

---

# 📸 Features

- Live DSLR / Webcam feed
- Draw finish line manually
- Supports multiple lanes (4–8+)
- Automatic motion detection per lane
- Timestamp for each athlete
- Ranking (who finished first)
- On‑screen timer
- Fullscreen UI
- Results panel
- Watermark support (`@akulsaju`)
- Works offline
- Can build into standalone `.exe`

---

# 🖥️ Demo Output (example)

Lane 4 → 12.84s → 1st
Lane 2 → 12.91s → 2nd
Lane 5 → 13.02s → 3rd
Lane 1 → 13.44s → 4th

yaml
Copy code

---

# ⚙️ Requirements

Install Python 3.10+

Then:

```bash
py -m pip install opencv-python numpy
📷 Camera Setup
Option A — DSLR
Use:

HDMI capture card

OR Canon EOS Webcam Utility

OR Nikon Webcam Utility

Option B — Webcam
Just plug and play.

▶️ Run
Open terminal in project folder:

bash
Copy code
python race_timer.py
or

bash
Copy code
py race_timer.py
🖱️ Controls
Key	Action
F	Fullscreen
R	Reset race
Q	Quit
Mouse	Draw finish line
Lanes	Set number of lanes in code

🎯 How it works
Camera placed sideways at finish line

Draw a vertical detection line

Each lane has its own region

Motion crossing line triggers timestamp

Software logs and ranks finishes

🧠 Detection Logic
Background subtraction

Motion threshold

Per‑lane ROI

First crossing = finish time

Sorted timestamps = ranking

📦 Build as EXE (App)
Install:

bash
Copy code
py -m pip install pyinstaller
Build:

bash
Copy code
py -m PyInstaller --onefile --noconsole race_timer.py
Output:

bash
Copy code
dist/race_timer.exe
Double click to run like normal app.

🗂️ Project Structure
Copy code
race-timer/
│
├─ race_timer.py
├─ README.md
(Simple single‑file project)

🎨 Tips for Accurate Timing
✅ Use 60+ FPS camera
✅ Place camera exactly perpendicular to finish line
✅ Use bright daylight
✅ Tight crop only finish area
✅ Avoid camera shake

📈 Accuracy
Typical:

30 FPS → ±0.03s

60 FPS → ±0.016s

120 FPS → ±0.008s

Good enough for school meets.

🚀 Future Ideas
Auto lane detection

CSV export

Photo finish zoom

Slow‑motion replay

Web dashboard

Multiple cameras

Cloud leaderboard

👤 Author
@akulsaju

Built for school athletics timing system.

📜 License
MIT — free to use and modify

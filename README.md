# 🏃 DSLR Race Timer (Finish Line Auto Detection)

A Python + OpenCV based **school athletics race timer** that uses a DSLR (or webcam) to automatically detect when athletes cross the finish line. It logs:

✅ Lane number  
✅ Finish time  
✅ Order (1st, 2nd, 3rd…)  
✅ Live video overlay  
✅ Works in real‑time  
✅ Windows compatible  
✅ Can export as `.exe` app  

---

## 📸 Features

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

## 🖥️ Demo Output (Example)

```plaintext
Lane 4 → 12.84s → 1st
Lane 2 → 12.91s → 2nd
Lane 5 → 13.02s → 3rd
Lane 1 → 13.44s → 4th
```

---

## ⚙️ Requirements

1. **Install Python 3.10+**

2. Then, install dependencies:

   ```bash
   py -m pip install opencv-python numpy
   ```

---

### 📷 Camera Setup

#### Option A — DSLR  
Use: 
- HDMI capture card  
- OR Canon EOS Webcam Utility  
- OR Nikon Webcam Utility  

#### Option B — Webcam  
Just plug and play.

---

### ▶️ Run  
Open terminal in the project folder and run:  

```bash
python race_timer.py
# or
py race_timer.py
```

---

### 🖱️ Controls

| **Key**  | **Action**                |
|----------|---------------------------|
| `F`      | Fullscreen                |
| `R`      | Reset race                |
| `Q`      | Quit                      |
| **Mouse**| Draw finish line          |
| **Code** | Set number of lanes       |

---

## 🎯 How It Works

1. Place the camera sideways at the finish line.  
2. Draw a vertical detection line.  
3. Each lane has its own region of interest (ROI).  
4. Motion crossing the line triggers a timestamp.  
5. Software logs and ranks finishes.  

---

## 🧠 Detection Logic

- Background subtraction  
- Motion threshold  
- Per-lane ROI  
- First crossing → Finish time  
- Sorted timestamps → Ranking  

---

## 📦 Build as EXE (App)

1. Install PyInstaller:

   ```bash
   py -m pip install pyinstaller
   ```

2. Build the app:

   ```bash
   py -m PyInstaller --onefile --noconsole race_timer.py
   ```

3. Output:

   ```bash
   dist/race_timer.exe
   ```

4. Double-click to run the `.exe` like a normal app.

---

## 🗂️ Project Structure

```plaintext
race-timer/
│
├─ race_timer.py
├─ README.md
```
(Single‑file project)

---

## 🎨 Tips for Accurate Timing

✅ Use a 60+ FPS camera  
✅ Place the camera exactly perpendicular to the finish line  
✅ Use bright daylight  
✅ Tight crop only on the finish area  
✅ Avoid camera shake  

---

## 📈 Accuracy

- 30 FPS → ±0.03s  
- 60 FPS → ±0.016s  
- 120 FPS → ±0.008s  

Good enough for school meets.

---

## 🚀 Future Ideas

- Auto lane detection  
- CSV export  
- Photo finish zoom  
- Slow‑motion replay  
- Web dashboard  
- Multiple cameras  
- Cloud leaderboard  

---

## 👤 Author

**@akulsaju**

Built for **school athletics timing system**.

---

## 📜 License

**MIT** — free to use and modify.

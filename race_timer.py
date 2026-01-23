import cv2
import numpy as np
import time
from collections import deque

# =============================
# SETTINGS
# =============================
LANES = 6
CAM_INDEX = 0
THRESH = 20

WINDOW_NAME = "Race Timer PRO"

# =============================
# CAMERA
# =============================
cap = cv2.VideoCapture(CAM_INDEX, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# =============================
# GLOBALS
# =============================
lane_lines = []
finish_segments = []
results = []
pts = []

mode = "lane"
status = "Draw 6 lanes"
start_time = None
prev_gray = None

buffer_frames = deque(maxlen=300)

lane_colors = [
    (255,0,0),(0,255,0),(0,0,255),
    (255,255,0),(255,0,255),(0,255,255)
]

# =============================
# MOUSE
# =============================
def mouse(event, x, y, flags, param):
    global pts, lane_lines, finish_segments, status

    if mode == "run":
        return

    if event == cv2.EVENT_LBUTTONDOWN:
        pts = [(x,y)]

    elif event == cv2.EVENT_LBUTTONUP:
        pts.append((x,y))

        if mode == "lane" and len(lane_lines) < LANES:
            lane_lines.append(tuple(pts))
            status = f"Lane {len(lane_lines)}/{LANES}"

        elif mode == "finish" and len(finish_segments) < LANES:
            finish_segments.append(tuple(pts))
            status = f"Finish {len(finish_segments)}/{LANES}"


# =============================
# WINDOW
# =============================
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WINDOW_NAME,
                      cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)

cv2.setMouseCallback(WINDOW_NAME, mouse)


# =============================
# MAIN LOOP
# =============================
while True:

    ret, frame = cap.read()
    if not ret:
        break

    buffer_frames.append(frame.copy())

    display = frame.copy()
    h, w = display.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(7,7),0)

    # =================================
    # MOTION DETECTION
    # =================================
    if mode == "run" and prev_gray is not None:

        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, THRESH, 255, cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh, None, iterations=2)

        for i, seg in enumerate(finish_segments):

            if i < len(results):
                continue

            mask = np.zeros_like(thresh)
            cv2.line(mask, seg[0], seg[1], 255, 12)

            movement = cv2.countNonZero(cv2.bitwise_and(thresh, mask))

            if movement > 200:
                t = time.time() - start_time
                results.append((i+1, t))
                status = f"Lane {i+1} finished"

    prev_gray = gray.copy()

    # =================================
    # DRAW LANES
    # =================================
    for i, line in enumerate(lane_lines):
        color = lane_colors[i % len(lane_colors)]
        cv2.line(display, line[0], line[1], color, 3)
        cv2.putText(display, f"L{i+1}", line[0],
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    for seg in finish_segments:
        cv2.line(display, seg[0], seg[1], (0,0,255), 5)

    # =================================
    # TOP BAR
    # =================================
    top_h = 90
    cv2.rectangle(display,(0,0),(w,top_h),(25,25,25),-1)

    cv2.putText(display, f"MODE: {mode.upper()}",
                (20,35),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    cv2.putText(display, status,
                (20,70),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)

    # big timer
    if start_time:
        elapsed = time.time()-start_time
        cv2.putText(display, f"{elapsed:06.3f}s",
                    (w-330,60),
                    cv2.FONT_HERSHEY_DUPLEX,1.6,(0,255,0),3)

    # =================================
    # BOTTOM RESULTS PANEL
    # =================================
    bottom_h = 140
    cv2.rectangle(display,(0,h-bottom_h),(w,h),(25,25,25),-1)

    x = 40
    for lane,t in results:
        cv2.putText(display, f"L{lane}: {t:.3f}s",
                    (x, h-60),
                    cv2.FONT_HERSHEY_DUPLEX,0.9,(0,255,0),2)
        x += 200

    # =================================
    # WATERMARK CREDIT
    # =================================
    watermark = "@akulsaju"
    (tw,th),_ = cv2.getTextSize(watermark,
                                cv2.FONT_HERSHEY_SIMPLEX,0.6,1)

    cv2.putText(display, watermark,
                (w - tw - 20, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX,0.6,(200,200,200),1)

    # =================================
    # SHOW
    # =================================
    cv2.imshow(WINDOW_NAME, display)

    key = cv2.waitKey(1) & 0xFF

    # =================================
    # CONTROLS
    # =================================
    if key == ord('q'):
        break

    elif key == ord('l'):
        lane_lines=[]
        mode="lane"
        status="Draw lanes"

    elif key == ord('f'):
        finish_segments=[]
        mode="finish"
        status="Draw finish segments"

    elif key == ord('s'):
        if len(finish_segments)==LANES:
            mode="run"
            results=[]
            start_time=time.time()
            status="Running..."

    elif key == ord('r'):
        for f in buffer_frames:
            cv2.imshow(WINDOW_NAME, f)
            cv2.waitKey(40)


cap.release()
cv2.destroyAllWindows()

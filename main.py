import cv2
import numpy as np
import pygame

CAMERA_URL = "http://192.168.1.4:8080/video"
ALARM_FILE = "alarm.mp3"

# Threshold minimal area (piksel²)
MIN_AREA_NORMAL = 3000    # objek dekat
MIN_AREA_FAR = 200        # objek jauh (lebih sensitif)

cap = cv2.VideoCapture(CAMERA_URL)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound(ALARM_FILE)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)
    kernel = np.ones((5,5),np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_DILATE, kernel)

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < MIN_AREA_FAR:
            continue  # skip noise kecil
        # objek jauh atau dekat
        motion_detected = True
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Kontrol alarm
    if motion_detected:
        if not pygame.mixer.get_busy():
            alarm_sound.play(-1)  # -1 supaya loop terus selama gerakan
    else:
        # Tidak ada gerakan, hentikan alarm
        alarm_sound.stop()

    cv2.imshow("Sensor Gerakan", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()

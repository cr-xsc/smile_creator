# -*- coding: utf-8 -*-
import cv2
import argparse
import time

# 引数の設定
parser = argparse.ArgumentParser(description='Smile Detector')
parser.add_argument('--camera', '-c', type=int, default=0, metavar='CAMERA_NUM', help='Camera number')
parser.add_argument('--csi', action='store_true', help='use CSI camera')
args = parser.parse_args()

# 顔検出用と笑顔検出用のカスケード分類器の読み込み
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('./haarcascade_smile.xml')

# カメラの設定
# カメラ設定
# Setting camera parameters
if args.csi or (args.camera < 0):
    # Open the MIPI-CSI camera
    GST_STR = 'nvarguscamerasrc sensor-id=0 \
    ! video/x-raw(memory:NVMM), width=800, height=600, format=(string)NV12, framerate=(fraction)30/1 \
    ! nvvidconv flip-method=0 ! video/x-raw, width=(int)800, height=(int)600, format=(string)BGRx \
    ! videoconvert ! video/x-raw, format=(string)BGR \
    ! appsink'

    cam = cv2.VideoCapture(GST_STR, cv2.CAP_GSTREAMER)
    time.sleep(1)  # 起動待ち
else:
    # Open the V4L2 camera
    cam = cv2.VideoCapture(args.camera)
    time.sleep(1)  # 起動待ち

while True:
    # フレームの取得
    ret, frame = cam.read()
    if not ret:
        print("Error: Cannot read frame")
        break

    # グレースケール変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顔検出
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # 顔を矩形で囲む
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 笑顔検出（顔領域内のみ）
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        for (sx, sy, sw, sh) in smiles:
            # 笑顔を矩形で囲む
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

    # 結果の表示
    cv2.imshow('Smile Detector', frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラ解放とウィンドウ終了
cam.release()
cv2.destroyAllWindows()

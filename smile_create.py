# -*- coding: utf-8 -*-
import cv2
import argparse
import time
import os
import random

# -----引数の設定-------------------------------------------
parser = argparse.ArgumentParser(description='Smile Detector')
parser.add_argument('--camera', '-c', type=int, default=0, metavar='CAMERA_NUM', help='Camera number')
parser.add_argument('--csi', action='store_true', help='use CSI camera')
args = parser.parse_args()
# ----------------------------------------------------------

# -----カスケード分類期の読み込み---------------------------
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('./haarcascade_smile.xml')
# ----------------------------------------------------------

# -----笑顔貼り付け処理の初期化-----------------------------
# ランダムに選ぶ画像が保存されているディレクトリを指定
image_dir = './smile_list'  # 貼り付け画像のディレクトリ
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
if not image_files:
    print("Error: No images found in the specified directory.")
    exit()
current_overlay = cv2.imread(random.choice(image_files), cv2.IMREAD_UNCHANGED)
last_smile_detected = False
# ----------------------------------------------------------

# -----カメラの設定-----------------------------------------
camera = 0  # 使用するカメラ番号
cam = cv2.VideoCapture(camera)
if not cam.isOpened():
    print("Error: Cannot open camera")
    exit()
# ----------------------------------------------------------


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

    # -----顔検出有無の画面表示-----------------------------
    if len(faces) > 0:
        status_text = "face_detecting"
        text_color = (0, 255, 0)  # 緑色
    else:
        status_text = "no face"
        text_color = (0, 0, 255)  # 赤色
    # テキストを画面上に描画
    cv2.putText(frame, status_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2, cv2.LINE_AA)
    # ------------------------------------------------------

    current_smile_detected = False
    for (x, y, w, h) in faces:
        # 笑顔の検出（顔領域内のみ）
        roi_gray = gray[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        # -----笑顔貼り付け処理-----------------------------
        if len(smiles) == 0:  # 笑顔が検出されない場合
            # 顔範囲に貼り付け画像をリサイズ
            resized_overlay = cv2.resize(current_overlay, (w, h), interpolation=cv2.INTER_AREA)
            overlay_region = frame[y:y + h, x:x + w]

            # アルファブレンドで画像を貼り付け
            if resized_overlay.shape[2] == 4:  # RGBA画像の場合
                alpha_mask = resized_overlay[:, :, 3] / 255.0
                for c in range(0, 3):  # RGBチャンネル
                    overlay_region[:, :, c] = (alpha_mask * resized_overlay[:, :, c] +
                                            (1 - alpha_mask) * overlay_region[:, :, c])
            else:  # RGB画像の場合
                overlay_region[:, :, :] = resized_overlay
        else:
            current_smile_detected = True
        # --------------------------------------------------

    # -----検知状態が途切れたら画像を切り替える処理---------
    if last_smile_detected and not current_smile_detected:
        current_overlay = cv2.imread(random.choice(image_files), cv2.IMREAD_UNCHANGED)
    last_smile_detected = current_smile_detected
    # ------------------------------------------------------

    # 結果の表示
    cv2.imshow('Smile Create', frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラ解放とウィンドウ終了
cam.release()
cv2.destroyAllWindows()

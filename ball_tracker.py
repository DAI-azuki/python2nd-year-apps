import cv2
import numpy as np


# スライダーを動かした瞬間に実行する関数を必ず1つ登録する必要がある
def nothing(x):
    pass


# 1. カメラ起動
camera = cv2.VideoCapture(0)

# 調整用のウィンドウを作る
cv2.namedWindow("Adjustment")

# 「明るさのしきい值」を変えるスライダーを作る (初期値200, 最大255)
cv2.createTrackbar("Threshold", "Adjustment", 200, 255, nothing)


while True:
    # retは撮影成功したかframeは写真そのもののデータ
    ret, frame = camera.read()
    if not ret:
        break

    #  グレースケール化　→　白黒へ
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # thersholdの値を取得
    thresh_val = cv2.getTrackbarPos("Threshold", "Adjustment")

    # 二値化 (thresholdの値より明るい所を白、それ以外を黒にする)
    _, mask = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

    # 輪郭を探す、cv2.RETR_TREE （全部拾う）、cv2.CHAIN_APPROX_SIMPLE （データ圧縮）
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # 小さいノイズは無視
        if cv2.contourArea(contour) > 100:
            # 重心（中心点）を計算
            M = cv2.moments(contour)

            # モーメントを面積で割って、重心を出している
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # 赤い丸とその座標を描画
            cv2.circle(frame, (cX, cY), 10, (0, 0, 255), -1)
            cv2.putText(
                frame,
                f"({cX}, {cY})",
                (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                2,
            )

    # 画面に表示
    cv2.imshow("Camera", frame)
    cv2.imshow("Mask (Black & White)", mask)  # 仕組み確認用

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()

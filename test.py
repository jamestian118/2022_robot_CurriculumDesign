import cv2

cap = cv2.VideoCapture(0)

while True:
    # 读取视频流中的一帧
    ret, frame = cap.read()

    # 如果读取视频流失败，退出循环
    if not ret:
        break

    # 将视频帧水平翻转
    frame = cv2.flip(frame, 1)

    # 显示翻转后的视频帧
    cv2.imshow('Video', frame)

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()

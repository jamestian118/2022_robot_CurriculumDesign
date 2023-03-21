# 考勤窗口
# 开始上课->人脸识别考勤->结束上课->统计考勤 未经人脸识别的absenteeism加1 计算addendance_rate
# 上课时不允许进行信息采集 按键不可按 ；未上课时不可进行人脸识别考勤 按键不可按
# 人脸识别时显示姓名、学号、缺勤次数、出勤率
# 点击信息采集后跳转至信息采集窗口
# 信息采集窗口可以查询学生所有信息（以学号来进行搜索）
#

from hashlib import new
import numpy as np
from matplotlib import pyplot as plt
import math
from sklearn import neighbors
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import cv2
import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QDateTime, QCoreApplication, QThread
from PyQt5.QtGui import QImage, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QInputDialog
import sys
from datetime import datetime
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
import cv2
import sys

# 引入本地文件
import global_value
import Dialog.data_management_system as data_management_system
import face_detection
import information_collection as information_collection
import UI.MainWindowUI as MainWindowUI
import dynamic_detection
from Dialog.InfoDialog import InfoDialog
from Dialog.RCDialog import RCDialog
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()
        # self.ui = MainUI.Ui_Form()
        self.ui = MainWindowUI.Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化label显示的(黑色)背景
        self.bkg_pixmap = QPixmap('./logo_imgs/bkg1.png')
        # 设置主窗口的logo
        self.logo = QIcon('./logo_imgs/fcb_logo.jpg')
        # 设置提示框icon
        self.info_icon = QIcon('./logo_imgs/info_icon.jpg')

        # 设置窗口名称和图标
        self.setWindowTitle('人脸识别考勤系统')
        self.setWindowIcon(self.logo)
        # 设置单张图片背景
        self.ui.label_camera.setPixmap(self.bkg_pixmap)
        # label_time显示系统时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time_text)
        # 启动时间任务
        self.timer.start()

        # 初始化摄像头，默认调用第一个摄像头
        self.url = 0
        self.cap = cv2.VideoCapture()

        # 设置摄像头按键连接函数
        self.ui.bt_open_camera.clicked.connect(self.open_camera)
        # 设置开始考勤按键的回调函数
        self.ui.bt_start_check.clicked.connect(self.auto_control)
        # 设置活体检测按键的回调函数
        self.ui.bt_blinks.clicked.connect(self.blinks_thread)
        # 设置“退出系统”按键事件, 按下之后退出主界面
        self.ui.bt_exit.clicked.connect(self.quit_window)
        # 设置信息采集按键连接
        self.ui.bt_gathering.clicked.connect(self.open_info_dialog)
        # 人脸识别按键连接
        self.ui.bt_check_variation.clicked.connect(self.detection)
        # 查看结果案件连接
        self.ui.bt_view.clicked.connect(self.check_result)

        # 设置区分打开摄像头还是人脸识别的标识符
        self.switch_bt = 0
        self.blink_flag = 0
        self.new_array = []
        self.trainer = 0

    def show_time_text(self):
        # 设置宽度
        self.ui.label_time.setFixedWidth(200)
        # 设置显示文本格式
        self.ui.label_time.setStyleSheet(
            # "QLabel{background:white;}" 此处设置背景色
            "QLabel{color:rgb(0, 0, 0); font-size:14px; font-weight:bold; font-family:宋体;}"
            "QLabel{font-size:14px; font-weight:bold; font-family:宋体;}")

        current_datetime = QDateTime.currentDateTime().toString()
        self.ui.label_time.setText("" + current_datetime)

        # 显示“人脸识别考勤系统”文字
        self.ui.label_title.setFixedWidth(400)
        self.ui.label_title.setStyleSheet(
            "QLabel{font-size:26px; font-weight:bold; font-family:宋体;}")
        self.ui.label_title.setText("人脸识别考勤系统")

    def open_camera(self):
        # 判断摄像头是否打开，如果打开则为true，反之为false
        if not self.cap.isOpened():
            self.ui.label_logo.clear()
            # 默认打开Windows系统笔记本自带的摄像头，如果是外接USB，可将0改成1
            self.cap.open(self.url)
            self.show_camera()
        else:
            self.cap.release()
            self.ui.label_logo.clear()
            self.ui.label_camera.clear()
            self.ui.bt_open_camera.setText(u'打开相机')

    def capture_image(self):
        self.ui.label_logo.clear()
        while self.cap.isOpened():
            ret, self.image = self.cap.read()
            # 告诉QT处理来处理任何没有被处理的事件，并且将控制权返回给调用者，让代码变的没有那么卡
            QApplication.processEvents()
            show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
            # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
            self.showImage = QImage(
                show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.ui.label_camera.setPixmap(
                QPixmap.fromImage(self.showImage))

            keyword = cv2.waitKey(1)
            if keyword == ord('s'):  # 按s保存当前图片
                cv2.imwrite('./test_img/knn_examples/test/test.jpg', self.image)
            elif keyword == ord('q'):  # 按q退出
                break

        # 因为最后会存留一张图像在lable上，需要对lable进行清理
        self.ui.label_camera.clear()

        # 释放窗口
        self.cap.release()
        cv2.destroyAllWindows()

    def dynamic_detection(self):
        # 定义一个计数器用于计算连续的眨眼次数
        blink_count = 0

        # 用于判断眼睛是否闭合
        def is_eye_closed(eye_points):
            # 计算眼睛纵横比 (aspect ratio)
            A = np.linalg.norm(eye_points[1] - eye_points[5])
            B = np.linalg.norm(eye_points[2] - eye_points[4])
            C = np.linalg.norm(eye_points[0] - eye_points[3])

            # 计算纵横比
            ear = (A + B) / (2.0 * C)

            # 判断眼睛是否闭合
            if ear < 0.25:
                return True
            return False

        if self.cap.isOpened():
            while True:
                ret, frame = self.cap.read()

                if not ret:
                    break

                QApplication.processEvents()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = detector(gray)

                for face in faces:
                    landmarks = predictor(gray, face)
                    landmarks = np.array([(p.x, p.y) for p in landmarks.parts()])

                    left_eye_points = landmarks[42:48]
                    right_eye_points = landmarks[36:42]

                    left_eye_closed = is_eye_closed(left_eye_points)
                    right_eye_closed = is_eye_closed(right_eye_points)

                    if left_eye_closed and right_eye_closed:
                        blink_count += 1
                        print(blink_count)
                    else:
                        blink_count = 0

                    if blink_count >= 3:
                        self.blink_flag = 1
                        self.ui.textBrowser_log.append('活体检测通过，可开始进行人脸识别!')
                        break

                if self.blink_flag:
                    break

                cv2.imshow("Camera", frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
        else:
            QMessageBox.information(self, "提示", "请先打开摄像头！", QMessageBox.Ok)

        cv2.destroyAllWindows()




    def show_camera(self):
        # 如果按键按下
        global embedded, le, recognizer
        if self.cap.isOpened():

            if self.switch_bt == 0:
                #
                self.ui.label_logo.clear()
                self.ui.bt_open_camera.setText(u'关闭相机')
                while self.cap.isOpened():
                    # 以BGR格式读取图像
                    ret, self.image = self.cap.read()
                    # 告诉QT处理来处理任何没有被处理的事件，并且将控制权返回给调用者，让代码变的没有那么卡
                    QApplication.processEvents()
                    # 检查图像是否读取成功
                    if self.image is None:
                        print("No frame captured, skipping frame processing.")
                        continue
                    # 将图像转换为RGB格式
                    show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                    # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                    self.showImage = QImage(
                        show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                    self.ui.label_camera.setPixmap(
                        QPixmap.fromImage(self.showImage))
                # 因为最后会存留一张图像在lable上，需要对lable进行清理
                self.ui.label_camera.clear()
                self.ui.bt_open_camera.setText(u'打开相机')
                # 设置单张图片背景
                self.ui.label_camera.setPixmap(self.bkg_pixmap)

            elif self.switch_bt == 1:
                self.ui.label_logo.clear()
                self.ui.bt_start_check.setText(u'退出考勤')

                self.capture_image()
                # 人脸识别考勤
                image_path = "./test_img/knn_examples/test/test.jpg"
                if self.trainer == 1:
                    # STEP 2201350211_fanzitian 训练KNN分类器
                    print("Training KNN classifier...")
                    classifier = face_detection.train("./test_img/knn_examples/train",
                                                      model_save_path="trained_knn_model.clf",
                                                      n_neighbors=2)
                    print("Training complete!")
                    self.trainer = 0

                # STEP 2 使用训练好的KNN分类器对测试的人脸图像进行识别
                face_detection.capture_image()
                image_file = os.path.join(image_path)
                # 待测试人脸图像路径
                full_file_path = os.path.join(image_path)
                print("Looking for faces in {}".format(image_file))
                # 用经过训练的分类器模型查找图像中的所有人
                predictions = face_detection.predict(
                    full_file_path, model_path="trained_knn_model.clf")
                # 打印结果
                for student_id, (top, right, bottom, left) in predictions:
                    # print("- Found {} at ({}, {})".format(student_id, left, top))
                    self.ui.textBrowser_log.append(
                        " {} 打卡成功！".format(student_id))
                if student_id == "unknown":
                    self.ui.textBrowser_log.append(" 未知人员！")
                else:
                    self.new_array.append(int(student_id[:10]))

                # 因为最后一张画面会显示在GUI中，此处实现清除。
                self.blink_flag = 0
                self.ui.label_camera.clear()

        else:
            QMessageBox.information(self, "Tips", "请先打开摄像头！", QMessageBox.Ok)

    def auto_control(self):
        if self.cap.isOpened():
            if self.switch_bt == 0:
                self.switch_bt = 1
                self.ui.bt_start_check.setText(u'退出考勤')

            elif self.switch_bt == 1:
                self.switch_bt = 0
                self.ui.bt_start_check.setText(u'开始考勤')

            else:
                print("[Error] The value of self.switch_bt must be zero or one!")
        else:
            QMessageBox.information(
                self, "Tips", "请先打开摄像头！", QMessageBox.Ok)

    def detection(self):
        if self.cap.isOpened():
            if self.switch_bt == 1:
                if self.blink_flag == 1:
                    self.show_camera()
                    self.blink_flag = 0
                else:
                    QMessageBox.information(
                        self, "Tips", "请先活体检测！", QMessageBox.Ok)
            else:
                QMessageBox.information(
                    self, "Tips", "请先开始考勤！", QMessageBox.Ok)

    def blinks_thread(self):
        self.blink_flag = 0
        if self.cap.isOpened():
            self.startThread = self.dynamic_detection()
            print('blinks_thread is running!')
            self.blink_flag = 1
            self.ui.textBrowser_log.append('活体检测通过，可开始进行人脸识别!')
            print('blinks_thread is finished!')

        else:
            QMessageBox.information(self, "Tips", "请先打开摄像头！", QMessageBox.Ok)

    def quit_window(self):
        if self.cap.isOpened():
            self.cap.release()
        QCoreApplication.quit()

    def open_info_dialog(self):
        self.trainer = 1
        if self.cap.isOpened():
            QMessageBox.warning(
                self, "Warning", "为防止摄像头冲突，已自动关闭摄像头！", QMessageBox.Ok)
            self.cap.release()

    def check_result(self):
        dict_from_csv = pd.read_csv('students_data.csv').to_dict()
        for i in range(len(dict_from_csv['id'])):
            if dict_from_csv['id'][i] not in self.new_array:
                self.ui.tableView_late.append(
                    " {} {} 未到！".format(dict_from_csv['id'][i], dict_from_csv['name'][i]))
        self.ui.lcd_1.display(len(dict_from_csv['id']))
        self.ui.lcd_2.display(len(self.new_array))
        print(self.new_array)
        print(dict_from_csv['id'][0])
        self.new_array = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 创建并显示窗口
    mainWindow = MainWindow()
    infoWindow = InfoDialog()
    rcWindow = RCDialog()
    mainWindow.ui.bt_gathering.clicked.connect(infoWindow.handle_click)
    mainWindow.ui.bt_random_check.clicked.connect(rcWindow.handle_click)
    mainWindow.show()
    sys.exit(app.exec_())

# 随机点名程序主界面
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
import random
# 导入本地文件
import UI.RandomCheckUI as RandomCheckUI
import global_value


class RCDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.Dialog = RandomCheckUI.Ui_Form()
        self.Dialog.setupUi(self)

        # 实现路径错误提示，方便定位错误
        self.current_filename = os.path.basename(__file__)

        try:
            # 设置窗口名称和图标
            self.setWindowTitle("随机点名答题系统")
            self.setWindowIcon(QIcon(
                f'/Volumes/exchange/macos/cc3a0fb70480bbc2120149a115ffe534_Visual_Studio_Code.icns'))
        except FileNotFoundError as e:
            print("[ERROR] UI背景图片路径不正确！(source file: {})".format(
                self.current_filename), e)
        else:
            print("[INFO] 设置icon成功！")

        self.Dialog.pb_start.clicked.connect(self.start_random_check)
        self.Dialog.pb_success.clicked.connect(self.success_answer)
        self.Dialog.pb_fail.clicked.connect(self.fail_answer)
        self.Dialog.pb_absentee.clicked.connect(self.absenteeism)

    def start_random_check(self):
        dict_from_csv = pd.read_csv('students_data.csv').to_dict()
        list_id = list(dict_from_csv['id'].values())
        list_random = list(range(0, len(list_id)))
        for n in range(len(list_id)):
            if dict_from_csv['absenteeism'][n] != 0:
                list_random.append(n + len(list_id))
        num = list_random[random.randint(0, len(list_random)-1)]

        if num >= len(list_id):
            num = num - len(list_id)
        student_id = list_id[num]
        name = dict_from_csv['name'][num]

        self.rc_name = name
        self.rc_id = student_id

        self.Dialog.lcdNumber_id.setText('{}'.format(int(student_id)))
        self.Dialog.textBrowser_name.setText('{}'.format(name))

        # 获取系统时间，保存到秒
        self.current_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def success_answer(self):
        global_value.student_comment.append('{}.{}{} answer_success'.format(
            global_value.number_of_courses, self.rc_id, self.rc_name))
        self.Dialog.window.setText(
            "{} {} {} 正确回答".format(self.rc_id, self.rc_name, self.current_time))

    def fail_answer(self):
        global_value.student_comment.append('{}.{}{} answer_fail'.format(
            global_value.number_of_courses, self.rc_id, self.rc_name))
        self.Dialog.window.setText(
            "{} {} {} 答题失败".format(self.rc_id, self.rc_name, self.current_time))

    def absenteeism(self):
        global_value.student_comment.append('{}.{}{} dont attend'.format(
            global_value.number_of_courses, self.rc_id, self.rc_name))
        student_id = int(self.rc_id)
        dict_from_csv = pd.read_csv('students_data.csv').to_dict()
        result_number = list(dict_from_csv['id'].values()).index(student_id)
        dict_from_csv['absenteeism'][result_number] = dict_from_csv['absenteeism'][result_number] + 1
        dict_from_csv['attendance_rate'][result_number] = 1 - dict_from_csv['absenteeism'][result_number] / \
            global_value.number_of_courses
        pd.DataFrame(dict_from_csv).to_csv('students_data_convert.csv')
        self.Dialog.window.setText(
            "{} {} {} 未到".format(self.rc_id, self.rc_name, self.current_time))

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def handle_click(self):
        if not self.isVisible():
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rcwindow = RCDialog()
    rcwindow.show()
    sys.exit(app.exec_())

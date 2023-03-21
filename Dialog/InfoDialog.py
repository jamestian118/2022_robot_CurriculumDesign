# 信息采集主界面
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
import imutils

import UI.information_gui as information_gui
import information_collection as information_collection
import global_value


class InfoDialog(QWidget):
    def __init__(self):
        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()

        self.Dialog = information_gui.Ui_Form()
        self.Dialog.setupUi(self)

        # 实现路径错误提示，方便定位错误
        self.current_filename = os.path.basename(__file__)

        try:
            # 设置窗口名称和图标
            self.setWindowTitle('个人信息采集')
            self.setWindowIcon(QIcon(
                f'/Users/fanzitian/Library/Mobile Documents/com~apple~CloudDocs/CODE/Python_code/2022_robot_CurriculumDesign/logo_imgs/fcb_logo.jpg'))

        except FileNotFoundError as e:
            print("[ERROR] UI背景图片路径不正确!(source file: {})".format(
                self.current_filename), e)

        # 设置信息采集按键连接函数
        self.Dialog.bt_start_collect.clicked.connect(self.open_camera)
        # 设置查询信息按键连接函数
        self.Dialog.bt_check_info.clicked.connect(self.check_info)
        # 设置修改信息按键连接函数
        self.Dialog.bt_change_info.clicked.connect(self.change_info)
        # 设置添加信息按键连接函数
        self.Dialog.bt_add_info.clicked.connect(self.add_info)

        # 初始化摄像头
        self.cap = cv2.VideoCapture(0)

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()

    def open_camera(self):
        self.dialog_text_id, ok_1 = QInputDialog.getText(
            self, '创建个人图像数据库', '请输入学号:')
        self.dialog_text_name, ok_2 = QInputDialog.getText(
            self, '创建个人图像数据库', '请输入姓名:')
        if ok_1 & ok_2:
            self.Dialog.label_capture.clear()
            self.cap.open(0)

        self.Dialog.label_capture.clear()
        print("[INFO] starting video stream...")

        information_collection.CatchPICFromVideo(
            "get face", 0, 99, self.dialog_text_name, self.dialog_text_id)

    def check_info(self):
        dict_from_csv = pd.read_csv('students_data.csv').to_dict()

        name = self.Dialog.lineEdit_name.text()
        student_id = int(self.Dialog.lineEdit_id.text())
        result_number = list(dict_from_csv['id'].values()).index(student_id)
        self.Dialog.tableView.append('{} {} {} {} 查询学生信息成功！'.format(
            dict_from_csv['name'][result_number], dict_from_csv['id'][result_number],
            dict_from_csv['absenteeism'][result_number], dict_from_csv['attendance_rate'][result_number]))

    def add_info(self):
        dict_from_csv = pd.read_csv('students_data.csv').to_dict()
        # 创建一个空字典
        new_student_info = {}
        # 输入学生信息
        new_student_info['name'] = self.Dialog.lineEdit_name.text()
        new_student_info['id'] = self.Dialog.lineEdit_id.text()
        new_student_info['absenteeism'] = 0
        new_student_info['attendance_rate'] = 0.0
        # 将学生信息添加到字典中
        dict_from_csv['name'][len(dict_from_csv['name'])] = (
            new_student_info['name'])
        dict_from_csv['id'][len(dict_from_csv['id'])] = (
            new_student_info['id'])
        dict_from_csv['absenteeism'][len(dict_from_csv['absenteeism'])] = (
            new_student_info['absenteeism'])
        dict_from_csv['attendance_rate'][len(dict_from_csv['attendance_rate'])] = (
            new_student_info['attendance_rate'])
        # 将字典转换为csv文件
        pd.DataFrame(dict_from_csv).to_csv('students_data.csv')
        self.Dialog.tableView.append('{} {} 添加学生信息成功！'.format(
            new_student_info['name'], new_student_info['id']))

    def change_info(self):
        dict_from_csv = pd.read_csv('students_data.csv')
        # 输入要修改的学生姓名
        name = self.Dialog.lineEdit_name.text()
    
        dict_from_csv = dict_from_csv.drop([list(
            (dict_from_csv.to_dict())['name'].values()).index(name)])
        dict_from_csv = dict_from_csv.to_dict()
        
        # 输入要修改的学生信息
        new_student_info = {}
        new_student_info['name'], ok = QInputDialog.getText(
            self, '修改学生信息', '请输入学生姓名：')
        new_student_info['id'], ok = QInputDialog.getText(
            self, '修改学生信息', '请输入学生学号：')
        str_absenteeism, ok = QInputDialog.getText(
            self, '修改学生信息', '请输入学生缺勤次数：')
        new_student_info['absenteeism'] = int(str_absenteeism)
        new_student_info['attendance_rate'] = (
            1 - (new_student_info['absenteeism']) / global_value.number_of_courses)

        # 将学生信息添加到字典中
        dict_from_csv['name'][len(dict_from_csv['name'])] = (
            new_student_info['name'])
        dict_from_csv['id'][len(dict_from_csv['id'])] = (
            new_student_info['id'])
        dict_from_csv['absenteeism'][len(dict_from_csv['absenteeism'])] = (
            new_student_info['absenteeism'])
        dict_from_csv['attendance_rate'][len(dict_from_csv['attendance_rate'])] = (
            new_student_info['attendance_rate'])
        # 将字典转换为csv文件
        pd.DataFrame(dict_from_csv).to_csv('students_data.csv')
        self.Dialog.tableView.append('{} {} {} {} 修改学生信息成功！'.format(
            new_student_info['name'], new_student_info['id'], new_student_info['absenteeism'], new_student_info['attendance_rate']))

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    infowindow = InfoDialog()
    infowindow.show()
    sys.exit(app.exec_())

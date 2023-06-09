
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 907)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setGeometry(QtCore.QRect(30, 80, 700, 600))
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(850, 20, 231, 30))
        self.label_time.setText("")
        self.label_time.setObjectName("label_time")

        self.tableView_late = QtWidgets.QTextBrowser(self.centralwidget)
        self.tableView_late.setGeometry(QtCore.QRect(860, 360, 211, 141))
        self.tableView_late.setObjectName("tableView_late")
        self.label_listName1 = QtWidgets.QLabel(self.centralwidget)
        self.label_listName1.setGeometry(QtCore.QRect(860, 340, 31, 16))
        self.label_listName1.setObjectName("label_listName1")

        self.textBrowser_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_log.setGeometry(QtCore.QRect(350, 690, 301, 161))
        self.textBrowser_log.setObjectName("textBrowser_log")

        self.bt_blinks = QtWidgets.QPushButton(self.centralwidget)
        self.bt_blinks.setGeometry(QtCore.QRect(770, 770, 71, 81))
        self.bt_blinks.setObjectName("bt_blinks")
        self.bt_start_check = QtWidgets.QPushButton(self.centralwidget)
        self.bt_start_check.setGeometry(QtCore.QRect(660, 770, 101, 81))
        self.bt_start_check.setObjectName("bt_start_check")
        self.bt_open_camera = QtWidgets.QPushButton(self.centralwidget)
        self.bt_open_camera.setGeometry(QtCore.QRect(660, 690, 181, 71))
        self.bt_open_camera.setObjectName("bt_open_camera")

        self.bt_view = QtWidgets.QPushButton(self.centralwidget)
        self.bt_view.setGeometry(QtCore.QRect(860, 680, 211, 51))
        self.bt_view.setObjectName("bt_view")
        self.bt_random_check = QtWidgets.QPushButton(self.centralwidget)
        self.bt_random_check.setGeometry(QtCore.QRect(860, 740, 211, 41))
        self.bt_random_check.setObjectName("bt_random_check")
        self.bt_exit = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exit.setGeometry(QtCore.QRect(860, 790, 211, 61))
        self.bt_exit.setObjectName("bt_exit")

        self.lcd_1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_1.setGeometry(QtCore.QRect(900, 140, 71, 31))
        self.lcd_1.setObjectName("lcd_1")
        self.lcd_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_2.setGeometry(QtCore.QRect(900, 180, 71, 31))
        self.lcd_2.setObjectName("lcd_2")
        self.label_lcdName1 = QtWidgets.QLabel(self.centralwidget)
        self.label_lcdName1.setGeometry(QtCore.QRect(860, 150, 31, 16))
        self.label_lcdName1.setObjectName("label_lcdName1")
        self.label_lcdName2 = QtWidgets.QLabel(self.centralwidget)
        self.label_lcdName2.setGeometry(QtCore.QRect(860, 190, 31, 16))
        self.label_lcdName2.setObjectName("label_lcdName2")
        self.bt_check = QtWidgets.QPushButton(self.centralwidget)
        self.bt_check.setGeometry(QtCore.QRect(980, 140, 91, 71))
        self.bt_check.setObjectName("bt_check")

        self.bt_check_variation = QtWidgets.QPushButton(self.centralwidget)
        self.bt_check_variation.setGeometry(QtCore.QRect(20, 760, 131, 61))
        self.bt_check_variation.setObjectName("bt_check_variation")
        self.bt_gathering = QtWidgets.QPushButton(self.centralwidget)
        self.bt_gathering.setGeometry(QtCore.QRect(20, 690, 131, 61))
        self.bt_gathering.setObjectName("bt_gathering")

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(360, 20, 400, 40))
        self.label_title.setText("")
        self.label_title.setObjectName("label_title")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(30, 70, 800, 600))
        self.label_logo.setMinimumSize(QtCore.QSize(800, 600))
        self.label_logo.setMaximumSize(QtCore.QSize(800, 600))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 60, 821, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(840, 70, 20, 781))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(150, 690, 31, 131))
        self.line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 833, 301, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")


       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSetting)
        self.menuFile.addAction(self.actionExport)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_random_check.setText(_translate("MainWindow", "随机点名"))
        self.bt_blinks.setText(_translate("MainWindow", "活体检测"))
        self.bt_start_check.setText(_translate("MainWindow", "开始考勤"))
        self.bt_view.setText(_translate("MainWindow", "查看结果"))
        self.label_lcdName2.setText(_translate("MainWindow", "实到"))
        self.bt_open_camera.setText(_translate("MainWindow", "打开相机"))
        self.bt_check.setText(_translate("MainWindow", "查询"))
        self.bt_exit.setText(_translate("MainWindow", "退出系统"))
        self.label_listName1.setText(_translate("MainWindow", "未到"))
        self.bt_gathering.setText(_translate("MainWindow", "信息采集"))
        self.label_lcdName1.setText(_translate("MainWindow", "应到"))
        self.bt_check_variation.setText(_translate("MainWindow", "人脸识别"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setWhatsThis(_translate("MainWindow", "Author: datamonday"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionExport.setText(_translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(260, 560)
        Form.setMinimumSize(QtCore.QSize(260, 560))
        Form.setMaximumSize(QtCore.QSize(260, 560))
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_name.setObjectName("label_name")
        self.label_id = QtWidgets.QLabel(Form)
        self.label_id.setGeometry(QtCore.QRect(20, 40, 71, 21))
        self.label_id.setObjectName("label_id")
        self.lineEdit_id = QtWidgets.QLineEdit(Form)
        self.lineEdit_id.setGeometry(QtCore.QRect(100, 40, 141, 21))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(100, 70, 141, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.bt_add_info = QtWidgets.QPushButton(Form)
        self.bt_add_info.setGeometry(QtCore.QRect(15, 430, 100, 41))
        self.bt_add_info.setObjectName("bt_add_info")
        self.bt_change_info = QtWidgets.QPushButton(Form)
        self.bt_change_info.setGeometry(QtCore.QRect(130, 430, 100, 41))
        self.bt_change_info.setObjectName("bt_add_info")
        self.bt_start_collect = QtWidgets.QPushButton(Form)
        self.bt_start_collect.setGeometry(QtCore.QRect(15, 510, 100, 41))
        self.bt_start_collect.setObjectName("bt_start_collect")
        self.bt_check_info = QtWidgets.QPushButton(Form)
        self.bt_check_info.setGeometry(QtCore.QRect(130, 510, 100, 41))
        self.bt_check_info.setObjectName("bt_check_info")

        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(40, 10, 251, 16))
        self.label_title.setObjectName("label_title")

        self.label_capture = QtWidgets.QLabel(Form)
        self.label_capture.setGeometry(QtCore.QRect(10, 40, 500, 400))
        self.label_capture.setMinimumSize(QtCore.QSize(500, 400))
        self.label_capture.setMaximumSize(QtCore.QSize(500, 400))
        self.label_capture.setText("")
        self.label_capture.setObjectName("label_capture")

        self.tableView = QtWidgets.QTextBrowser(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 100, 221, 291))
        self.tableView.setObjectName("tableView")
        self.label_name.raise_()
        self.label_id.raise_()
        self.bt_start_collect.raise_()
        self.label_title.raise_()
        self.bt_check_info.raise_()
        self.bt_add_info.raise_()
        self.bt_change_info.raise_()
        self.label_capture.raise_()
        self.lineEdit_id.raise_()
        self.lineEdit_name.raise_()
        self.tableView.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.bt_start_collect, self.lineEdit_id)
        Form.setTabOrder(self.lineEdit_id, self.lineEdit_name)
        Form.setTabOrder(self.lineEdit_name, self.bt_check_info)
        Form.setTabOrder(self.bt_check_info, self.bt_add_info)
        Form.setTabOrder(self.bt_add_info, self.bt_change_info)
        Form.setTabOrder(self.bt_change_info, self.tableView)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "请输入姓名："))
        self.label_id.setText(_translate("Form", "请输入学号："))
        self.bt_add_info.setText(_translate("Form", "添加信息"))
        self.bt_change_info.setText(_translate("Form", "修改信息"))
        self.bt_start_collect.setText(_translate("Form", "开始采集"))
        self.label_title.setText(_translate("Form", "人脸识别个人信息采集系统"))
        self.bt_check_info.setText(_translate("Form", "查询信息"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

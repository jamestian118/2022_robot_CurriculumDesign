
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 300)
        self.pb_success = QtWidgets.QPushButton(Form)
        self.pb_success.setGeometry(QtCore.QRect(50, 160, 101, 41))
        self.pb_success.setObjectName("pb_success")
        self.pb_fail = QtWidgets.QPushButton(Form)
        self.pb_fail.setGeometry(QtCore.QRect(190, 160, 101, 41))
        self.pb_fail.setObjectName("pb_fail")
        self.pb_start = QtWidgets.QPushButton(Form)
        self.pb_start.setGeometry(QtCore.QRect(100, 20, 301, 41))
        self.pb_start.setObjectName("pb_start")
        self.pb_absentee = QtWidgets.QPushButton(Form)
        self.pb_absentee.setGeometry(QtCore.QRect(330, 160, 101, 41))
        self.pb_absentee.setObjectName("pb_absence")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 90, 31, 41))
        self.label.setObjectName("label")
        self.label_id = QtWidgets.QLabel(Form)
        self.label_id.setGeometry(QtCore.QRect(40, 90, 31, 41))
        self.label_id.setObjectName("label_id")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(280, 90, 171, 31))
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.lcdNumber_id = QtWidgets.QTextBrowser(Form)
        self.lcdNumber_id.setGeometry(QtCore.QRect(80, 90, 171, 41))
        self.lcdNumber_id.setObjectName("lcdNumber_id")
        self.textBrowser_name = QtWidgets.QTextBrowser(Form)
        self.textBrowser_name.setGeometry(QtCore.QRect(310, 90, 141, 41))
        self.textBrowser_name.setObjectName("textBrowser_name")

        self.window = QtWidgets.QTextBrowser(Form)
        self.window.setGeometry(QtCore.QRect(30, 240, 420, 41))
        self.window.setObjectName("window")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_success.setText(_translate("Form", "成功回答"))
        self.label.setText(_translate("Form", "姓名"))
        self.pb_fail.setText(_translate("Form", "答题失败"))
        self.label_id.setText(_translate("Form", "学号"))

        self.pb_start.setText(_translate("Form", "随机点名"))
        self.pb_absentee.setText(_translate("Form", "未到"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

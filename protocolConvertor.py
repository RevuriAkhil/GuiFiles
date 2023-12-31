# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'protocolConvertor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
from time import sleep


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(559, 345)
        Dialog.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalWidget = QtWidgets.QWidget(Dialog)
        self.verticalWidget.setGeometry(QtCore.QRect(40, 50, 131, 171))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.verticalWidget.setFont(font)
        self.verticalWidget.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"background-color: rgb(85, 170, 255);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.verticalWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_4 = QtWidgets.QFrame(self.verticalWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label_3 = QtWidgets.QLabel(self.verticalWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(180, 50, 121, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        #line edit
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.line_2 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.line_3 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(160, 50, 20, 171))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 170, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CAN"))
        self.label_2.setText(_translate("Dialog", "RS 485"))
        self.label_3.setText(_translate("Dialog", "RS 232"))
        self.label_4.setText(_translate("Dialog", "Transmit"))
        self.label_5.setText(_translate("Dialog", "Received"))
        self.label_6.setText(_translate("Dialog", "Transmit"))
        self.label_7.setText(_translate("Dialog", "Received"))
        self.label_8.setText(_translate("Dialog", "Transmit"))
        self.label_9.setText(_translate("Dialog", "Received"))
        
        self.pushButton.setText(_translate("Dialog", "SEND"))
        self.pushButton_2.setText(_translate("Dialog", "SEND"))
        self.pushButton_3.setText(_translate("Dialog", "SEND"))

        #Action for buttons
        self.pushButton.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton_3.clicked.connect(self.on_pushButton3_clicked)

        # try:
        try:
            ser = serial.Serial('COM12', 9600,timeout=1)
        except:
            print("COM port not connected")
            raise SystemExit("Program aborted") #Exit exxecution

        #while 1:
        try:
            rs = ser.readline().decode("utf-8")
        
            if(rs != None and rs[0] == "1"):
                print("response:"+rs[1])
                self.lineEdit_2.setText(rs[1])
                #break
            if(rs != None and rs[0] == "2"):
                self.lineEdit_6.setText(rs[1])
                print("response:"+rs[1])
                #break
            if(rs != None and rs[0] == "3"):
                self.lineEdit_4.setText(rs[1])
                print("response:"+rs[1])
                #break
        except IndexError:
            print("Not getting value")


        # except IndexError as e:
        #     print("Not getting value from sensor")


    def on_pushButton1_clicked(self):
        line_edit_value = self.lineEdit.text() 
        print("transmitting: 1"+line_edit_value)
        self.waitForResponse()
    def on_pushButton2_clicked(self):
        line_edit_value = self.lineEdit_5.text() 
        print("transmitting: 2"+line_edit_value)
        self.waitForResponse()
    def on_pushButton3_clicked(self):
        line_edit_value = self.lineEdit_3.text() 
        print("transmitting: 3"+line_edit_value)
        self.waitForResponse()

    def waitForResponse(self,):
        #print("in wait")
        ser = serial.Serial('COM5', 9600,timeout=1)  # Replace 'COM4' with your actual port and set the appropriate baud rate

        #while 1:
        rs = ser.readline().decode("utf-8")
        
        if(rs != None and rs[0] == "1"):
            print("response:"+rs[1])
            self.lineEdit_2.setText(rs[1])
            #self.lineEdit_2.setText(rs)
            # break
        if(rs != None and rs[0] == "2"):
            self.lineEdit_6.setText(rs[1])
            print("response:"+rs[1])
            # break
        if(rs != None and rs[0] == "3"):
            self.lineEdit_4.setText(rs[1])
            print("response:"+rs[1])
            # break


        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

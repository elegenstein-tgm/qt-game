__author__ = 'fusions'
import sys, csv
from PyQt5 import QtCore, QtGui, QtWidgets
from gameui import Ui_MainWindow
import random

class MyDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter = 0;
        # init gui
        self.setdefinit()
        self.dorandbuttons()
        self.buttcon()
        self.ui.pushButton_16.clicked.connect(self.restart)

    @staticmethod
    def gen15random():
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        random.shuffle(items)
        return items

    def dorandbuttons(self):
        bvals = self.gen15random()
        self.ui.pushButton.setText(str(bvals[0]))
        self.ui.pushButton_2.setText(str(bvals[1]))
        self.ui.pushButton_3.setText(str(bvals[2]))
        self.ui.pushButton_4.setText(str(bvals[3]))
        self.ui.pushButton_5.setText(str(bvals[4]))
        self.ui.pushButton_6.setText(str(bvals[5]))
        self.ui.pushButton_7.setText(str(bvals[6]))
        self.ui.pushButton_8.setText(str(bvals[7]))
        self.ui.pushButton_9.setText(str(bvals[8]))
        self.ui.pushButton_10.setText(str(bvals[9]))
        self.ui.pushButton_11.setText(str(bvals[10]))
        self.ui.pushButton_12.setText(str(bvals[11]))
        self.ui.pushButton_13.setText(str(bvals[12]))
        self.ui.pushButton_14.setText(str(bvals[13]))
        self.ui.pushButton_15.setText(str(bvals[14]))
        self.ui.pushButton.setObjectName("b" + str(bvals[0]))
        self.ui.pushButton_2.setObjectName("b" + str(bvals[1]))
        self.ui.pushButton_3.setObjectName("b" + str(bvals[2]))
        self.ui.pushButton_4.setObjectName("b" + str(bvals[3]))
        self.ui.pushButton_5.setObjectName("b" + str(bvals[4]))
        self.ui.pushButton_6.setObjectName("b" + str(bvals[5]))
        self.ui.pushButton_7.setObjectName("b" + str(bvals[6]))
        self.ui.pushButton_8.setObjectName("b" + str(bvals[7]))
        self.ui.pushButton_9.setObjectName("b" + str(bvals[8]))
        self.ui.pushButton_10.setObjectName("b" + str(bvals[9]))
        self.ui.pushButton_11.setObjectName("b" + str(bvals[10]))
        self.ui.pushButton_12.setObjectName("b" + str(bvals[11]))
        self.ui.pushButton_13.setObjectName("b" + str(bvals[12]))
        self.ui.pushButton_14.setObjectName("b" + str(bvals[13]))
        self.ui.pushButton_15.setObjectName("b" + str(bvals[14]))

    def buttcon(self):
        self.ui.pushButton.clicked.connect(self.clicklistener)
        self.ui.pushButton_2.clicked.connect(self.clicklistener)
        self.ui.pushButton_3.clicked.connect(self.clicklistener)
        self.ui.pushButton_4.clicked.connect(self.clicklistener)
        self.ui.pushButton_5.clicked.connect(self.clicklistener)
        self.ui.pushButton_6.clicked.connect(self.clicklistener)
        self.ui.pushButton_7.clicked.connect(self.clicklistener)
        self.ui.pushButton_8.clicked.connect(self.clicklistener)
        self.ui.pushButton_9.clicked.connect(self.clicklistener)
        self.ui.pushButton_10.clicked.connect(self.clicklistener)
        self.ui.pushButton_11.clicked.connect(self.clicklistener)
        self.ui.pushButton_12.clicked.connect(self.clicklistener)
        self.ui.pushButton_13.clicked.connect(self.clicklistener)
        self.ui.pushButton_14.clicked.connect(self.clicklistener)
        self.ui.pushButton_15.clicked.connect(self.clicklistener)

    def setdefinit(self):
        self.ui.l_offen_val.setText("15")
        self.ui.l_falsch_val.setText("0")
        self.ui.l_korrekt_val.setText("0")
        self.ui.l_gesamt_val.setText("0")
        self.ui.l_spiele_val.setText("0")

    def clicklistener(self):
        self.ui.l_gesamt_val.setText(str(int(self.ui.l_gesamt_val.text())+1))
        self.counter += 1
        sending_button = self.sender()
        wasCorrect = False
        #print(str(sending_button.text()))
        if str(sending_button.text()) != str(self.counter):
            self.ui.l_falsch_val.setText(str(int(str(self.ui.l_falsch_val.text()))+1))
            self.counter -= 1
        else:
            self.ui.l_korrekt_val.setText(str(int(self.ui.l_korrekt_val.text())+1))
            self.ui.l_offen_val.setText(str(int(self.ui.l_offen_val.text())-1))
            wasCorrect = True
        #if wasCorrect:
        sending_button.setDisabled(wasCorrect)
        if int(str(sending_button.text())) == 15:
            self.ui.l_spiele_val.setText(str(int(str(self.ui.l_spiele_val.text()))+1))

    def restart(self):
        numgames = int(self.ui.l_spiele_val.text()) + 1
        self.setdefinit()
        self.dorandbuttons()
        self.ui.l_spiele_val.setText((str(numgames)))
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_8.setEnabled(True)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_12.setEnabled(True)
        self.ui.pushButton_13.setEnabled(True)
        self.ui.pushButton_14.setEnabled(True)
        self.ui.pushButton_15.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())

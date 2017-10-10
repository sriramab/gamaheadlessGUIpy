import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Helloworld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()

        label = QLabel("GAMA Headless Mode xml file")
        line_edit = QLineEdit("")
        button = QPushButton("Close")

        layout.addWidget(label,0,0)
        layout.addWidget(line_edit,0,1)
        layout.addWidget(button,1,1)



        # layout box properties
        self.setLayout(layout)
        self.setWindowTitle("GAMA Headless Mode GUI")

        button.clicked.connect(self.sriram)
        line_edit.textChanged.connect(label.setText)

    def sriram(self):
        print(sys.platform)


app = QApplication(sys.argv)
dialog=Helloworld()
dialog.show()
app.exec_()





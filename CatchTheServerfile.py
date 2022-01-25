"""

CTS [Open Source]
Catch! The! Serverfile!
Copyright 2022. sjrjq all rights reserved.

"""

from PyQt5.QtWidgets import *
import sys
import os


VirusDB = [
    'kro.kr',
    'codns',
    'kro'
]

vdb = []

filelist = [None]

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    
    def setupUI(self):
        
        self.setGeometry(500,500,500,500)
        self.setWindowTitle("CTS [Open Source]")
 
        self.OnOpenDocument_Button = QPushButton("파일 열기")
        self.OnOpenDocument_Button.clicked.connect(self.OnOpenDocument)

        self.Button2 = QPushButton("검사")
        self.Button2.clicked.connect(self.letsgo)

        self.label = QLabel()
        self.label.setText("검사 결과 :")

        self.label2 = QLabel()
        self.label2.setText("Copyright 2022. sjrjq all rights reserved.")

        layout = QVBoxLayout()
        layout.addWidget(self.OnOpenDocument_Button)
        layout.addWidget(self.Button2)
        layout.addWidget(self.Button3)
        layout.addWidget(self.label)
        layout.addWidget(self.label2)

        self.setLayout(layout)
 
    def OnOpenDocument(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "", "All Files(*);; PE files(*.exe)")
        if fname[0]:
            filelist[0] = fname[0]
        else:
            QMessageBox.about(self, "Warning!", "Please select file.")

    def letsgo(self):
        file = open(filelist[0], "rb")

        rded = file.readlines()

        x = str(rded).replace('\\x00','')


        for pattern in VirusDB:
            a = x.find(pattern)
            vdb.append(a)

        for i in range(len(vdb)):
            if vdb[i] != -1:
                self.label.setText("발견됨 : "+VirusDB[1])
                os.remove(filelist[0])
                vdb.clear()
                break
            else:
                self.label.setText("발견되지 않음")
                vdb.clear()
                break
            
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
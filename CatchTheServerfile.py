"""

CTS [Open Source]
Catch! The! Serverfile!
Copyright 2022. sjrjq all rights reserved.

"""

from PyQt5.QtWidgets import *
import sys
import re
import datetime




VirusDB = [
    'codns:DOMAIN',
    'Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run:SetStartup',
    'SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run:SetStartup',
    'kro.kr:DOMAIN',
    'HARDWARE\\Description\\System\\SystemProductName:grabPCinfo',
    'HARDWARE\\Description\\System\\SystemProductName:grabPCinfo',
    '\\x13[ENTER]:njrat_payload_src',
    '\\x1bprocesshacker\\x0bdnSpy:njrat_payload_src2',
    '\\x07\\x04\\x02\\x02\\x12\\x80\\x91\\x12\\x80\\x91/\\x07\\x13\\x0e\\x1d\\x0e\\x1d\\x0e:njratASM'
]


vdb = []

filelist = [None]

STATUS_CODE = None

for pattern in VirusDB:
    vdb.append(pattern)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    
    def setupUI(self):
        
        self.setGeometry(500,500,500,100)
        self.setWindowTitle("CTS [Open Source]")
 
        self.OnOpenDocument_Button = QPushButton("파일 열기")
        self.OnOpenDocument_Button.clicked.connect(self.OnOpenDocument)

        self.Button2 = QPushButton("검사")
        self.Button2.clicked.connect(self.letsgo)

        self.label = QLabel()
        self.label.setText("...")

        self.label2 = QLabel()
        self.label2.setText("Copyright 2022. sjrjq all rights reserved.")

        layout = QVBoxLayout()
        layout.addWidget(self.OnOpenDocument_Button)
        layout.addWidget(self.Button2)
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

        now = datetime.datetime.now()
        datem = str(now.strftime('%Y-%m-%d %H%M%S'))+'.log'

        file = open(filelist[0], "rb")
        file2 = open("log/"+datem, "w")
        FP = open("A.txt", "w")
        rded = file.readlines()

        x = str(rded).replace('\\x00','')
        
        FP.write(x)

        for i in vdb:
            px = i.split(':')
            if x.find(px[0]) == -1:
                file2.write('[not found]  ' + i + '\n')
            else:
                file2.write('[found]  ' + i + '\n')
        self.label.setText("스캔이 완료되었습니다. " + datem + "를 확인하세요.")
                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
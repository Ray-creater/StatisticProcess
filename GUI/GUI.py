import sys 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
import Component as cp

class Mywindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.mainWidget=QWidget()
        self.centralLayout=QVBoxLayout()
        self.mainWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.mainWidget)

        self.chooseLayout=QFormLayout()
        self.centralLayout.addLayout(self.chooseLayout)

        self.datFilePathButton=QPushButton("Choose .dat File Path")
        self.lableDatFile=QLabel('None')
        self.chooseLayout.addRow(self.datFilePathButton,self.lableDatFile)
        self.logFilePathButton=QPushButton('Choose .log File Path')
        self.lableLogFile=QLabel('None')
        self.chooseLayout.addRow(self.logFilePathButton,self.lableLogFile)

        self.lablePlot=QLabel('Pictrue\'s location')
        self.centralLayout.addWidget(self.lablePlot)

        self.functionLayout=QHBoxLayout()
        self.centralLayout.addLayout(self.functionLayout)
        self.readButton=QPushButton('Read Data')
        self.functionLayout.addWidget(self.readButton)
        self.plotButton=QPushButton('plot')
        self.functionLayout.addWidget(self.plotButton)


        self.message=QTextEdit()
        self.message.append('>>>Program Start')
        self.centralLayout.addWidget(self.message)
        self.message.setMaximumHeight(200)
        

        self.datFilePathButton.clicked.connect(self.chooseDatFile)
        self.logFilePathButton.clicked.connect(self.chooseLogFile)
        self.readButton.clicked.connect(self.readData)
        self.plotButton.clicked.connect(self.plot)



        self.setGeometry(200,125,1500,800)
        self.setWindowTitle('Analysis')
        self.show()


    def chooseDatFile(self):
        path,ok=QFileDialog.getOpenFileName(self,)
        if ok:
            self.lableDatFile.setText(str(path))

    def chooseLogFile(self):
        path,ok=QFileDialog.getOpenFileName(self,)
        if ok:
            self.lableLogFile.setText(str(path))

    def readData(self):
        if self.lableLogFile.text()=='None':
            pass
        else:
            self.component=cp.CurrentComponent(self.lableDatFile.text(),self.lableLogFile.text())
            self.message.append('>>>Read compelete')

    def plot(self):
        self.component.visualData(1,1,1)
        pic=QPixmap('1.png')
        self.lablePlot.setPixmap(pic)
        self.message.append('>>>Plot complete')

    




def main():
    app=QApplication(sys.argv)
    mywindow=Mywindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import sys 
from PyQt5 import QtCore,QtWidgets,QtGui
import hysteresis as hy

class Mywindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        datFilePathButton=QtWidgets.QPushButton("Choose .dat File Path",self)
        logFilePathButton=QtWidgets.QPushButton('Choose .log File Path',self)
        readButton=QtWidgets.QPushButton('Read Data',self)
        plotButton=QtWidgets.QPushButton('plot',self)
        
        self.lableDatFile=QtWidgets.QLabel('None')
        self.lableLogFile=QtWidgets.QLabel('None')
        self.lableRead=QtWidgets.QLabel('None')
        self.lablePlot=QtWidgets.QLabel('Pictrue\'s location')

        datFilePathButton.clicked.connect(self.chooseDatFile)
        logFilePathButton.clicked.connect(self.chooseLogFile)
        readButton.clicked.connect(self.readData)
        plotButton.clicked.connect(self.plot)


        vbox1=QtWidgets.QVBoxLayout()
        hbox=QtWidgets.QHBoxLayout()
        vbox2=QtWidgets.QVBoxLayout()


        vbox1.addWidget(datFilePathButton)
        vbox1.addWidget(self.lableDatFile)
        vbox1.addStretch(5)
        vbox1.addWidget(self.lablePlot)
        vbox1.addStretch(5)
        vbox1.addWidget(readButton)
        vbox1.addWidget(plotButton)
        vbox1.addWidget(self.lableRead)


        vbox2.addWidget(logFilePathButton)
        vbox2.addWidget(self.lableLogFile)
        vbox2.addStretch(10)

        hbox.addLayout(vbox1)
        hbox.addStretch(1)
        hbox.addLayout(vbox2)
        hbox.addStretch(10)

        self.setLayout(hbox)

        self.setGeometry(300,300,1000,600)
        self.setWindowTitle('Analysis')
        self.show()


    def chooseDatFile(self):
        path,ok=QtWidgets.QFileDialog.getOpenFileName(self,)
        if ok:
            self.lableDatFile.setText(str(path))

    def chooseLogFile(self):
        path,ok=QtWidgets.QFileDialog.getOpenFileName(self,)
        if ok:
            self.lableLogFile.setText(str(path))

    def readData(self):
        if self.lableDatFile.text()=='None' or self.lableLogFile.text()=='None':
            pass
        else:
            self.component=hy.CurrentComponent(self.lableDatFile.text(),self.lableLogFile.text())
            self.lableRead.setText('Read compelete')

    def plot(self):
        if self.lableRead.text()=='None':
            pass
        else:
            self.lableRead.setText('Loading Data')
            self.component.visualData(1,1,1)
            pic=QtGui.QPixmap('1.png')
            self.lablePlot.setPixmap(pic)
            self.lableRead.setText('Plot complete')

    




def main():
    app=QtWidgets.QApplication(sys.argv)
    mywindow=Mywindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
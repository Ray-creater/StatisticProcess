import sys 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
import Component as cp
from PyQt5.QtCore import Qt

class Mywindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.wholeWidget=QWidget()
        self.wholeWidgetLayout=QHBoxLayout()
        self.wholeWidget.setLayout(self.wholeWidgetLayout)
        self.setCentralWidget(self.wholeWidget)

        #Hysteresis plot area
        self.hysteresisWidget=QWidget()
        self.hysteresisWidgetLayout=QVBoxLayout()
        self.hysteresisWidget.setLayout(self.hysteresisWidgetLayout)
        self.wholeWidgetLayout.addWidget(self.hysteresisWidget)

        self.hysteresisWidgetTitle=QLabel('Plot Area:')
        self.hysteresisWidgetLayout.addWidget(self.hysteresisWidgetTitle,alignment=Qt.AlignCenter)
        self.chooseLayout=QFormLayout()
        self.chooseLayout.setFormAlignment(Qt.AlignCenter)
        self.hysteresisWidgetLayout.addLayout(self.chooseLayout)

        self.datFilePathButton=QPushButton("Choose .dat File Path")
        self.lableDatFile=QLabel('None')
        self.chooseLayout.addRow(self.datFilePathButton,self.lableDatFile)
        self.logFilePathButton=QPushButton('Choose .log File Path')
        self.lableLogFile=QLabel('None')
        self.chooseLayout.addRow(self.logFilePathButton,self.lableLogFile)

        self.lablePlot=QLabel('Pictrue\'s location')
        self.hysteresisWidgetLayout.addWidget(self.lablePlot,alignment=Qt.AlignCenter)

        self.functionLayout=QHBoxLayout()
        self.functionLayout.setAlignment(Qt.AlignCenter)
        self.hysteresisWidgetLayout.addLayout(self.functionLayout)
        self.readButton=QPushButton('Read Data')
        self.readButton.setMaximumWidth(100)
        self.functionLayout.addWidget(self.readButton,alignment=Qt.AlignLeft)
        self.plotButton=QPushButton('plot')
        self.plotButton.setMaximumWidth(100)
        self.functionLayout.addWidget(self.plotButton,alignment=Qt.AlignLeft)
        self.checkBoxListStr=['Hysteresis','Skeleton']
        self.checkBoxList=[QCheckBox(i) for i in self.checkBoxListStr]
        for i in self.checkBoxList:
            self.functionLayout.addWidget(i,alignment=Qt.AlignLeft)

        self.message=QTextEdit()
        self.message.append('>>>Program Start')
        self.hysteresisWidgetLayout.addWidget(self.message)
        self.message.setMaximumHeight(100)
        
        self.datFilePathButton.clicked.connect(self.chooseDatFile)
        self.logFilePathButton.clicked.connect(self.chooseLogFile)
        self.readButton.clicked.connect(self.readData)
        self.plotButton.clicked.connect(self.plot)
        ##Hysteresis stretch adjust
        self.hysteresisStretchList=[1,1,4,1]
        for i,j in enumerate(self.hysteresisStretchList):
            self.hysteresisWidgetLayout.setStretch(i,j)



        #ParaCalculate Area
        self.paraWidget=QWidget()
        self.wholeWidgetLayout.addWidget(self.paraWidget,alignment=Qt.AlignCenter)
        self.paraWidgetLayout=QVBoxLayout()
        self.paraWidget.setLayout(self.paraWidgetLayout)

        self.paraWidgetTitle=QLabel('Parameter Calculate:')
        self.paraWidgetLayout.addWidget(self.paraWidgetTitle,alignment=Qt.AlignCenter)
        self.paraLayout=QFormLayout()
        self.paraWidgetLayout.addLayout(self.paraLayout)
        self.labelListStr=['Yield Displacement','Yield Force','Peak Displacement','Peak Force','Ultimate Displacement','Ultimate Force','Ductlity Factor']
        self.labelList=[QLabel(i) for i in self.labelListStr]
        self.labelValue=[QLineEdit() for i in self.labelList]
        for i,j in zip(self.labelList,self.labelValue):
            self.paraLayout.addRow(i,j)
        self.yieldMethodLayout=QHBoxLayout()
        self.paraWidgetLayout.addLayout(self.yieldMethodLayout)
        self.yieldMethodLayout.setAlignment(Qt.AlignLeading)
        self.yieldMethodLable=QLabel('Yield Method Choose:')
        self.yieldMethodLayout.addWidget(self.yieldMethodLable)
        self.yieldMethodRadioButtonStr=['Area','Geometry','Rpart']
        self.yieldMethodRadioButton=[QRadioButton(i) for i in self.yieldMethodRadioButtonStr]
        for i in self.yieldMethodRadioButton:
            self.yieldMethodLayout.addWidget(i)

        ##caculate button
        self.caculateButton=QPushButton('Calculate')
        self.paraWidgetLayout.addWidget(self.caculateButton,alignment=Qt.AlignCenter)



        # Whole layout adjust
        self.wholeWidgetLayout.setStretch(0,4)
        self.wholeWidgetLayout.setStretch(1,1)

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
        if self.checkBoxList[0].isChecked() and not self.checkBoxList[1].isChecked():
            self.component.visualData(0,1,1)
            pic=QPixmap('1.png')
            self.lablePlot.setPixmap(pic)
            self.message.append('>>>Plot complete')
        elif not self.checkBoxList[0].isChecked() and self.checkBoxList[1].isChecked():
            self.component.visualData(1,0,1)
            pic=QPixmap('1.png')
            self.lablePlot.setPixmap(pic)
            self.message.append('>>>Plot complete')
        elif self.checkBoxList[0].isChecked() and self.checkBoxList[1].isChecked():
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
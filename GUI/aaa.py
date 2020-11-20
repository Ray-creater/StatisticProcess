import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
import qtawesome

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout()
        self.addLeftWidget()
        self.show()
        

    def layout(self):
        self.setGeometry(400,250,1000,600)
        self.mainWidget=QtWidgets.QWidget()
        self.mainLayout=QtWidgets.QGridLayout()
        self.mainWidget.setLayout(self.mainLayout)

        self.leftWidget=QtWidgets.QWidget()
        self.leftWidget.setObjectName('left widget')
        self.leftLayout=QtWidgets.QGridLayout()
        self.leftWidget.setLayout(self.leftLayout)

        self.rightWidget=QtWidgets.QWidget()
        self.rightWidget.setObjectName('right widget')
        self.rightLayout=QtWidgets.QGridLayout()
        self.rightWidget.setLayout(self.rightLayout)

        self.mainLayout.addWidget(self.leftWidget,0,0,12,2)
        self.mainLayout.addWidget(self.rightWidget,0,2,12,10)
        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle('Teaching Tool')

    def addLeftWidget(self):
        self.leftClose=QtWidgets.QPushButton("")
        self.leftVisit=QtWidgets.QPushButton("")
        self.leftMini=QtWidgets.QPushButton("")
        self.flexure=QtWidgets.QPushButton("Flexure")
        self.compression=QtWidgets.QPushButton("Compression")
        self.tension=QtWidgets.QPushButton('Tension') 

        self.chooseLabel=QtWidgets.QLabel('Choose component')
        self.chooseBeam=QtWidgets.QRadioButton('Beam')
        self.chooseColumns=QtWidgets.QRadioButton('Columns')
        self.chooseBeam.setCheckable(True)
        
        

        self.leftLayout.addWidget(self.leftClose,0,0,1,1)
        self.leftLayout.addWidget(self.leftVisit,0,1,1,1)
        self.leftLayout.addWidget(self.leftMini,0,2,1,1)
        self.leftLayout.addWidget(self.chooseBeam,3,0,1,1)
        self.leftLayout.addWidget(self.chooseColumns,3,1,1,2)
        self.leftLayout.addWidget(self.flexure,6,0,1,3)
        self.leftLayout.addWidget(self.compression,7,0,1,3)
        self.leftLayout.addWidget(self.tension,8,0,1,3)
    
    def beamLayout(self):
        pass

    

    def columnLayout(self):
        pass

        
        

def main():
    app =QtWidgets.QApplication(sys.argv)

    mw=mywindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QMenu,QTextEdit
from PyQt5.QtGui import QIcon

class mywindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction('Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(QApplication.quit)
        exitAct.setStatusTip('Exit app')


        self.statusBar()

        meunbar=self.menuBar()
        fileMenu=meunbar.addMenu('File')
        fileMenu.addAction(exitAct)
        menu2=QMenu('add a menu',self)
        fileMenu.addMenu(menu2)

        toolbar=self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('main window')
        self.show()

def main():
    app =QApplication(sys.argv)

    mw=mywindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import sys
from PyQt5.QtWidgets import QApplication,QWidget

from myApp import myAPP

if __name__=="__main__":
    app=QApplication(sys.argv)
    myWidget=myAPP()
    myWidget.show()
    sys.exit(app.exec_())
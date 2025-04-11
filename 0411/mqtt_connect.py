from PyQt5.QtWidgets import QWidget,QApplication, QPushButton, QVBoxLayout,\
    QLineEdit, QTextBrowser, QTextEdit
import sys
from PyQt5.Qt import QHBoxLayout
#mosquitto_sub -h localhost -t /central/DHT/room1
#mosquitto_pub -h localhost -t /central/DHT/room1 -m '{"dht":["room1",25.8,53.0]}'
#{"dht":["room1",25.8,54.0]}
class mainWidget(QWidget):
    def __init__(self):
        super().__init__()
        ledit = QLineEdit("192.168.1.14")
        vlayout = QVBoxLayout()
        vlayout.addWidget(ledit)
        tb = QTextEdit()
        
        vlayout.addWidget(tb)
        tb.setSizeIncrement(500, 500)
        #tb.setText("124\n456\n789")
        tb.append("123")
        tb.append("456")
        
        
        self.setLayout(vlayout)

app = QApplication(sys.argv)
#mywdiget = QWidget()
mywdiget = mainWidget()
mywdiget.show()
app.exec()
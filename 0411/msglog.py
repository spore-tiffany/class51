import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QDateTime

class LogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Log 範例")
        self.resize(400, 300)

        # 建立介面元件
        self.layout = QVBoxLayout()
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)  # 設定為唯讀
        self.btn_add_log = QPushButton("新增訊息")

        # 加入元件
        self.layout.addWidget(self.log_box)
        self.layout.addWidget(self.btn_add_log)
        self.setLayout(self.layout)

        # 設定按鈕事件
        self.btn_add_log.clicked.connect(self.add_log)

    def add_log(self):
        # 取得現在時間
        time_str = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        msg = f"[{time_str}] 這是一則日誌訊息"
        self.log_box.append(msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogWindow()
    window.show()
    sys.exit(app.exec_())

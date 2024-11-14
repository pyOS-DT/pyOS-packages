import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super(SimpleBrowser, self).__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("Simple Browser")
        self.setGeometry(300, 100, 1200, 800)

        # 创建浏览器视图
        self.browser = QWebEngineView()
        self.browser.setUrl("https://www.baidu.com")

        # 创建工具栏
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # 创建地址栏
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # 创建导航按钮
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        self.toolbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        self.toolbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        self.toolbar.addAction(home_btn)

        # 将地址栏添加到工具栏
        self.toolbar.addWidget(self.url_bar)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 更新地址栏
        self.browser.urlChanged.connect(self.update_url_bar)

    def navigate_home(self):
        self.browser.setUrl("https://www.google.com")

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.browser.setUrl(url)

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = SimpleBrowser()
    main_window.show()
    sys.exit(app.exec_())
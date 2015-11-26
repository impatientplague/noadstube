from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout
from PyQt4.QtWebKit import QWebView, QWebSettings
from PyQt4.QtCore import *

from ui_youtube import Ui_MainWindow
import pafy
import sys

QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)



url = 'https://www.youtube.com/watch?v=IdS3bWxG2a0&list=PLpclVninnGnvmdEPiApiIzt7Fe6GtRq5J'
video = pafy.new(url)

best = video.getbest()
bestvid = best.url
print bestvid

title = video.title

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle(title)

layout = QVBoxLayout()
win.setLayout(layout)

# Create and fill a QWebView
view = QWebView()
view.settings().setAttribute(QWebSettings.PluginsEnabled,True)
view.setHtml('''<html>
<body>

<iframe width="420" height="345"
src="%s">
</iframe>

</body>
</html>''' % bestvid)

layout.addWidget(view)

win.show()
app.exec_()

from PyQt4 import QtGui
from PyQt4.QtCore import QThread
from PyQt4.QtWebKit import QWebView, QWebSettings
from ui_youtube import Ui_MainWindow
import pafy
import sys
import logging
#from download_url import DownloadVideo

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
logging.disable(logging.DEBUG)

class NoAdsTube(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(NoAdsTube, self).__init__(parent)
        self.setupUi(self)
        self.download_url = DownloadVideo
        self.pushButton.clicked.connect(self.Download)
        self.push_url.clicked.connect(self.WatchVideo)

    def Download(self):
        url = self.lineEdit.text()
        self.get_thread = DownloadVideo(url)
        self.get_thread.start()

    def WatchVideo(self):
        try:
           video = pafy.new(self.lineEdit.text())
        except ValueError:
            logging.info('[Debug]: Not a Video Url')
            return
        title = video.title
        views = video.viewcount
        likes = video.likes
        dislikes = video.dislikes
        see = video.getbest()
        urlb = see.url
        self.setWindowTitle(title)
        self.views.setText(str(views))
        self.likes.setText(str(likes))
        self.likes_2.setText(str(dislikes))
        self.webView.settings().setAttribute(QWebSettings.PluginsEnabled,True)
        self.webView.setHtml('''<html>
<body>

<iframe width="440" height="220"
src="%s">
</iframe>

</body>
</html>''' % urlb)
        logging.info('[Debug]: Watching Video')


class DownloadVideo(QThread):
    def __init__(self , url):
        QThread.__init__(self)
        self.url = url

    def __del__(self):
        self.wait()

    def call_progress(self, total, recvd, ratio, rate, eta):
        if recvd == total:
            logging.info('[Debug]: Download Complete')

    def get_url(self):
        v = pafy.new(self.url)
        l = v.getbest()
        return l

    def run(self):
        vid = self.get_url()
        print("Size is %s" % vid.get_filesize())
        filename = vid.download(quiet=True,callback=self.call_progress)


def main():
    app = QtGui.QApplication(sys.argv)
    form = NoAdsTube()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()


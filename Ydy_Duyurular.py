#!/usr/bin/env python3
#mr-Ucar - A simple Python script with a Gui to follow the latest announcements from the School`s Official Website

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from bs4 import BeautifulSoup
import requests

class TabWidget(QTabWidget):
    """Set tup the tab and windows layout"""
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        self.setWindowTitle("DEUYDY")
      # (Arkadaslar, yuksekokulun icon`unu internetten indirip, kendi bilgisayarinizdaki konuma gore burda ayarlama yapin ki hata vermesin.)
      # Arrange here accordingly (Download the School icon and give the path of the downloaded icon as a .png or .jpg file)
        self.setWindowIcon(QIcon('/home/Ucar/ForMyClasses/Projects/Deu Yydy icon.png'))
        self.setTabsClosable(True)
        self.tabCloseRequested.connect( self.close_current_tab )
        self.setDocumentMode(True)
        width = 600 #If you want you can increase or reduce the default size settings here.
        height = 500 #If you want you can increase or reduce the default size settings here.
        self.setMinimumSize(width, height)
        baseurl = "https://ydy.deu.edu.tr/tr/duyurular"
        url = QUrl((baseurl))
        reqs = requests.get(baseurl)
        sp = BeautifulSoup(reqs.text, 'html.parser')
        tlt = sp.title.string
        view = HtmlView(self)
        view.load(url)
        ix = self.addTab(view, tlt)
    def close_current_tab(self, i):
        if self.count()<2:
            return
        self.removeTab(i)

class HtmlView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.tab = self.parent()

    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            webView = HtmlView(self.tab)
            baseurl = "https://ydy.deu.edu.tr/tr/duyurular"
            reqs = requests.get(baseurl)
            sp = BeautifulSoup(reqs.text, 'html.parser')
            tlt = sp.title.string
            ix = self.tab.addTab(webView, tlt)
            self.tab.setCurrentIndex(ix)
            return webView
        return QWebEngineView.createWindow(self, windowType)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = TabWidget()
    main.show()
    sys.exit(app.exec_())


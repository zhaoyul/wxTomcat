#!/bin/evn python
# -*- coding: UTF-8 -*-
import wx
import glob
from PIL import Image
from PropSpliter import ProportionalSplitter
from splitPanel import SplitPanel

#project import
from appStuff import plotPanel, MySplitter

#####################################################
# Interface
#####################################################
APP_TITLE=u"HIS管理平台"
MINI_SIZE=(480, 300)
#####################################################
# tomcat_directorys
#####################################################
#catidr=

def getNextImageID(count):
    imID = 0
    while True:
        yield imID
        imID += 1
        if imID == count:
            imID = 0


#左侧边栏
class MainTreeBook(wx.Treebook):
    def __init__(self, parent):
        wx.Treebook.__init__(self, parent, -1, style=wx.BK_DEFAULT)
        il = wx.ImageList(32, 32)
        il.Add(wx.Bitmap("appsrv.bmp", wx.BITMAP_TYPE_BMP))#web server icon
        for x in  range(3):
            il.Add(wx.Bitmap("tomcat.bmp", wx.BITMAP_TYPE_BMP))
        il.Add(wx.Bitmap("DB.bmp", wx.BITMAP_TYPE_BMP))#web server icon

        self.AssignImageList(il)
        imageIdGenerator = getNextImageID(il.GetImageCount())

        self.AddPage(AppServerStatus(self), u'应用服务器状态',
                imageId=imageIdGenerator.next())
        pages = [(AppNotebook(self), "8080"),
                 (AppNotebook(self), "8090"),
                 (AppNotebook(self), "9000")]
        for page, label in pages:
            self.AddSubPage(page, label, imageId=imageIdGenerator.next())

        self.AddPage(DBServerStatus(self), u'DB服务器状态',
                imageId=imageIdGenerator.next())

        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGING, self.OnPageChanging)

        #This is a workaround for a sizing bug on Mac...
        wx.FutureCall(100, self.AdjustSize)

    def AdjustSize(self):
        self.GetTreeCtrl().InvalidateBestSize()
        self.SendSizeEvent()

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanged, old:%d, new:%d, sel:%d\n' % (old, new,sel)
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanged, old:%d, new:%d, sel:%d\n' % (old, new,sel)
        event.Skip()

#主框架
class HISFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, APP_TITLE, size=(1024,768))
        MainTreeBook(self)
        self.CreateStatusBar()
        #status info
        self.PushStatusText(u"百灵his管理系统 版本 1.0.13")
        #put the app on the center of the screen
        self.Centre()

#启动画面
class HisSplashScreen(wx.SplashScreen):
    def __init__(self, parent=None):
        aBitmap = wx.Image(name = "SplashScreen.png").ConvertToBitmap()
        splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT
        splashDuration = 6000 # milliseconds
        # Call the constructor with the above arguments in exactly the
        # following order.
        wx.SplashScreen.__init__(self, aBitmap, splashStyle,
                                 splashDuration, parent)
        self.Bind(wx.EVT_CLOSE, self.OnExit)
        wx.Yield()

    def OnExit(self, evt):
        self.Hide()
        # MyFrame is the main frame.
        MyFrame = HISFrame()
        app.SetTopWindow(MyFrame)
        MyFrame.Show(True)
        # The program will freeze without this line.
        evt.Skip()  # Make sure the default handler runs too...
        return True

#应用服务器主页面
class AppServerStatus(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)

        #Attributes
        self.SetMinSize(MINI_SIZE)
        self.status = wx.Panel(self)
        self.monitor = plotPanel(self)
        self.createNewInst = wx.Panel(self)
        self.upgrade = wx.Panel(self)

        # Setup
        self.AddPage(self.status, u"实例状态")
        self.AddPage(self.monitor, u"即时监控")
        self.AddPage(self.createNewInst, u"创建实例")
        self.AddPage(self.upgrade, u"发布新版本")

#DB服务器主页面
class DBServerStatus(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)

        #Attributes
        self.SetMinSize(MINI_SIZE)
        self.status = wx.Panel(self)
        self.status1 = wx.Panel(self)
        self.status2 = wx.Panel(self)
        self.status3 = wx.Panel(self)
        self.status4 = wx.Panel(self)
        self.bk_rst = wx.Panel(self)

        # Setup
        self.AddPage(self.status, u"DB状态")
        self.AddPage(self.status1, u"表空间")
        self.AddPage(self.status2, u"读写")
        self.AddPage(self.status3, u"会话")
        self.AddPage(self.status4, u"数据对象")
        self.AddPage(self.bk_rst, u"备份还原")

#单个应用服务器页面
class AppNotebook(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)

        #Attributes
        self.SetMinSize(MINI_SIZE)
        self.status = SplitPanel(self)
        self.port = SplitPanel(self)
        self.port.SetBackgroundColour(wx.BLUE)
        self.parmeter = SplitPanel(self)
        self.fbrowser = wx.GenericDirCtrl(self)
        self.spliter = MySplitter(self, -1).createOne()

        # Setup
        self.AddPage(self.status, u"运行状态")
        self.AddPage(self.port, u"端口配置")
        self.AddPage(self.fbrowser, u"数据库管理")
        self.AddPage(self.parmeter, u"参数配置")
        self.AddPage(self.spliter,u'日志')


    def onStart(self, event):
        pass

class HISApp(wx.App):
    def OnInit(self):
        MySplash = HisSplashScreen()
        MySplash.Show()
        return True

if __name__ == '__main__':
    app = HISApp()
    app.MainLoop()

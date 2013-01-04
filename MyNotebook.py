#!/bin/evn python
# -*- coding: UTF-8 -*-
import wx

#####################################################
# Interface
#####################################################
APP_TITLE=u"HIS管理平台"
#####################################################
# tomcat_directorys
#####################################################
#catidr=



class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, APP_TITLE, size=(960,600))
        nb = MyNotebook(self)


class MyNotebook(wx.Notebook):
    def __init__(self, parent):
        super(MyNotebook, self).__init__(parent)

        #Attributes
        self.status = wx.Panel(self)
        self.port = wx.Panel(self)
        self.port.SetBackgroundColour(wx.BLUE)
        self.parmeter = wx.Panel(self)
        self.fbrowser = wx.GenericDirCtrl(self)

        # Setup
        self.AddPage(self.status, u"运行状态")
        self.AddPage(self.port, u"端口配置")
        self.AddPage(self.fbrowser, u"数据库管理")
        self.AddPage(self.parmeter, u"参数配置")

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
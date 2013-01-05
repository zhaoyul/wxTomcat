#!/bin/evn python
# -*- coding: UTF-8 -*-
import wx

#####################################################
# Interface
#####################################################
APP_TITLE=u"HIS管理平台"
MINI_SIZE=(480, 300)
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
        self.SetMinSize(MINI_SIZE)
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

        # tab status
        sizer = wx.GridBagSizer(hgap=5, vgap=5)
        self.status.SetSizer(sizer)
        startbtn = wx.Button(parent=self.status,label=u"启动", pos=(10, 10))
        sizer.Add(startbtn,pos=(0,3), span=(3,1), flag=wx.EXPAND)
        startbtn.Bind(wx.EVT_BUTTON, self.onStart)
        stopbtn = wx.Button(parent=self.status,label=u"停止", pos=(10, 10))
        sizer.Add(stopbtn,pos=(3,3), span=(3,1), flag=wx.EXPAND)
        stopbtn.Bind(wx.EVT_BUTTON, self.onStart)
        self.status.Fit()

    def onStart(self, event):
        pass


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()

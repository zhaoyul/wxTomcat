# -*- coding: UTF-8 -*-
import sys
import wx

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)

class SplitPanel(wx.SplitterWindow):
    def __init__(self, parent):
        wx.SplitterWindow.__init__(self, parent, -1,
                                   style = wx.SP_LIVE_UPDATE)

        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChanged)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING, self.OnSashChanging)

        sty = wx.BORDER_SUNKEN
        p1 = wx.Panel(self, style=sty, size = (100, 600))
        #p1.SetBackgroundColour("pink")
        wx.StaticText(p1, -1, "server log....", (5,5))

        #log should be scrollable...
        p2 = wx.Panel(self, style=sty)
        #p2.SetBackgroundColour("sky blue")
        log = wx.TextCtrl(p2, wx.ID_ANY, size=(300,100),
                          style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)

        # Add widgets to a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL|wx.EXPAND, 5)
        p2.SetSizer(sizer)

        # redirect text here
        redir=RedirectText(log)
        sys.stdout=redir
        sys.stderr=redir

        self.SetMinimumPaneSize(20)
        self.SplitHorizontally(p1, p2)


    def OnSashChanged(self, evt):
        print "sash changed to %s\n" % str(evt.GetSashPosition())

    def OnSashChanging(self, evt):
        print "sash changing to %s\n" % str(evt.GetSashPosition())
        # uncomment this to not allow the change
        #evt.SetSashPosition(-1)



if __name__ == "__main__":
    class TestFrame(wx.Frame):
        def __init__(self, parent, title):
            wx.Frame.__init__(self, parent, title=title, size = (200, 200))
            self.frame = SplitPanel(self)
            #self.frame.createOne()
    app = wx.App()
    frame = TestFrame(None, "hello, world")
    frame.Show()
    app.MainLoop()

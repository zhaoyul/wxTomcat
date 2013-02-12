# -*- coding: UTF-8 -*-
import numpy
import wx
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

#图表页面
class plotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, size=(50, 50))

        self.figure = matplotlib.figure.Figure()
        self.axes = self.figure.add_subplot(411)
        t = numpy.arange(0.0,  10, 1.0)
        s = [0,1, 0, 1, 0, 2, 1, 2, 1, 0]
        self.y_max = 10
        self.axes.plot(t, s)

        self.axes = self.figure.add_subplot(412)
        t = numpy.arange(0.0,  10, 1.0)
        s = [0,1, 0, 1, 0, 2, 1, 2, 1, 0]
        self.y_max = 10
        self.axes.plot(t, s)

        self.axes = self.figure.add_subplot(414)
        t = numpy.arange(0.0,  10, 1.0)
        s = [0,1, 0, 1, 0, 2, 1, 2, 1, 0]
        self.y_max = 10
        self.axes.plot(t, s)

        self.canvas = FigureCanvas(self, -1, self.figure)

#日志页面
class MySplitter(wx.SplitterWindow):
    def __init__(self, parent, ID ):
        wx.SplitterWindow.__init__(self, parent, ID,
                                   style = wx.SP_LIVE_UPDATE
                                   )
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChanged)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING, self.OnSashChanging)

    def OnSashChanged(self, evt):
        print "sash changed to %s\n" % str(evt.GetSashPosition())

    def OnSashChanging(self, evt):
        print "sash changing to %s\n" % str(evt.GetSashPosition())
        # uncomment this to not allow the change
        #evt.SetSashPosition(-1)

    def createOne(self):
        sty = wx.BORDER_SUNKEN
        p1 = wx.Window(self, style=sty)
        p1.SetBackgroundColour("pink")
        wx.StaticText(p1, -1, "server log....", (5,5))

        p2 = wx.Window(self, style=sty)
        p2.SetBackgroundColour("sky blue")
        wx.StaticText(p2, -1, "Access log....", (5,5))

        self.SetMinimumPaneSize(20)
        self.SplitVertically(p1, p2, -100)
        return self

if __name__ == "__main__":
    class TestFrame(wx.Frame):
        def __init__(self, parent, title):
            wx.Frame.__init__(self, parent, title=title, size = (200, 200))
            self.frame = plotPanel(self)
    app = wx.App()
    frame = TestFrame(None, "hello, world")
    frame.Show()
    app.MainLoop()

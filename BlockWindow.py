import wx
class myFrame(wx.Frame):
    def __init__(self, panel):
        wx.Frame__init__(self, None, -1, "Frame", size=(300,300)
class BlockWindow(wx.Panel):
    def __init__(self, parent, ID=-1, label="",
            pos=wx.DefaultPosition, size=(100,25)):
        self.label = label
        self.SetBackgroundColour("white")
        self.SetMiniSize(size)

app = wx.PySimpleApp()
frame = wx.Frame()


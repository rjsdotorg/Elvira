#Boa:MDIParent:MDIParentFrame1

import wx

def create(parent):
    return MDIParentFrame1(parent)

[wxID_MDIPARENTFRAME1] = [wx.NewId() for _init_ctrls in range(1)]

class MDIParentFrame1(wx.MDIParentFrame):
    def _init_ctrls(self, prnt):
        wx.MDIParentFrame.__init__(self, style=wx.DEFAULT_FRAME_STYLE | wx.VSCROLL | wx.HSCROLL, name='', parent=prnt, title='MDIParentFrame1', id=wxID_MDIPARENTFRAME1, pos=wx.Point(-1, -1), size=wx.Size(-1, -1))

    def __init__(self, parent):
        self._init_ctrls(parent)

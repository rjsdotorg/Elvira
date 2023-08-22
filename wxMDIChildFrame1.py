#Boa:MDIChild:wxMDIChildFrame1

import wx

def create(parent):
    return wxMDIChildFrame1(parent)

[wxID_WXMDICHILDFRAME1, wxID_WXMDICHILDFRAME1LISTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class wxMDIChildFrame1(wx.MDIChildFrame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MDIChildFrame.__init__(self, id=wxID_WXMDICHILDFRAME1, name='',
              parent=prnt, pos=wx.Point(38, 49), size=wx.Size(531, 362),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Ray')
        self.SetClientSize(wx.Size(523, 328))
        self.SetIcon(wx.Icon(u'icons/Eudora_368.ico',
              wx.BITMAP_TYPE_ICO))

        self.listCtrl1 = wx.ListCtrl(id=wxID_WXMDICHILDFRAME1LISTCTRL1,
              name='listCtrl1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(523, 328), style=wx.SUNKEN_BORDER | wx.LC_REPORT)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.index = 0
        self.listCtrl1.InsertColumn(0, 'S')
        self.listCtrl1.InsertColumn(1, 'Att')
        self.listCtrl1.InsertColumn(2, 'Who')
        self.listCtrl1.InsertColumn(3, 'Date')
        self.listCtrl1.InsertColumn(4, 'Subject')
        self.add_line()

    def add_line(self, event=None):
        self.listCtrl1.InsertStringItem(self.index, '.')
        self.listCtrl1.SetStringItem(self.index, 2, "TG")
        self.listCtrl1.SetStringItem(self.index, 3, "08:40 PM 8/30/2012")
        self.listCtrl1.SetStringItem(self.index, 4, "RE: Delivery Status Notification (Failure)")
        self.index += 1

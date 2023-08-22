#Boa:MDIParent:wxMDIParentFrame1

import wx
from wx.lib.anchors import LayoutAnchors

import wxMDIChildFrame1

def create(parent):
    return wxMDIParentFrame1(parent)

[wxID_WXMDIPARENTFRAME1, wxID_WXMDIPARENTFRAME1LISTCTRL1, 
 wxID_WXMDIPARENTFRAME1LISTVIEW1, wxID_WXMDIPARENTFRAME1LISTVIEW2, 
 wxID_WXMDIPARENTFRAME1NOTEBOOK1, wxID_WXMDIPARENTFRAME1SASHLAYOUTWINDOW1, 
 wxID_WXMDIPARENTFRAME1STATUSBAR1, wxID_WXMDIPARENTFRAME1TOOLBAR1, 
 wxID_WXMDIPARENTFRAME1TREECTRL1, wxID_WXMDIPARENTFRAME1TREECTRL2, 
] = [wx.NewId() for _init_ctrls in range(10)]

[wxID_WXMDIPARENTFRAME1TOOLBAR1TOOLS2, 
 wxID_WXMDIPARENTFRAME1TOOLBAR1TOOLSDELETE, 
] = [wx.NewId() for _init_coll_toolBar1_Tools in range(2)]

[wxID_WXMDIPARENTFRAME1MENUFILEITEMS0] = [wx.NewId() for _init_coll_menuFile_Items in range(1)]

class wxMDIParentFrame1(wx.MDIParentFrame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'File')
        parent.Append(menu=self.menuEdit, title=u'Edit')
        parent.Append(menu=self.menuMailbox, title=u'Mailbox')
        parent.Append(menu=self.menuMessage, title=u'Message')
        parent.Append(menu=self.menuTransfer, title=u'Transfer')
        parent.Append(menu=self.menuSpecial, title=u'Special')
        parent.Append(menu=self.menuTools, title=u'Tools')
        parent.Append(menu=self.menuWindow, title=u'Window')
        parent.Append(menu=self.menuHelp, title=u'Help')

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='Items0', id=wxID_WXMDIPARENTFRAME1MENUFILEITEMS0,
              kind=wx.ITEM_NORMAL, text='New child window')
        self.Bind(wx.EVT_MENU, self.OnMenuFileitems0Menu,
              id=wxID_WXMDIPARENTFRAME1MENUFILEITEMS0)

    def _init_coll_toolBar1_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wx.Bitmap(u'gifs/Eudora32_25027.gif',
              wx.BITMAP_TYPE_GIF), bmpDisabled=wx.NullBitmap,
              id=wxID_WXMDIPARENTFRAME1TOOLBAR1TOOLSDELETE, kind=wx.ITEM_NORMAL,
              label=u'', longHelp=u'', shortHelp=u'Delete Message(s)')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wx.Bitmap(u'gifs/Eudora32_72.gif',
              wx.BITMAP_TYPE_GIF), bmpDisabled=wx.NullBitmap,
              id=wxID_WXMDIPARENTFRAME1TOOLBAR1TOOLS2, kind=wx.ITEM_NORMAL,
              label='', longHelp=u'', shortHelp=u'Inbox')

        parent.Realize()

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.treeCtrl1, select=True,
              text=u'Mailboxes')
        parent.AddPage(imageId=-1, page=self.treeCtrl2, select=False,
              text=u'File Browser')
        parent.AddPage(imageId=-1, page=self.listView1, select=False,
              text=u'Signatures')
        parent.AddPage(imageId=-1, page=self.listView2, select=False,
              text=u'Stationary')
        parent.AddPage(imageId=-1, page=self.listCtrl1, select=False,
              text=u'Personalities')

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(7)

        parent.SetStatusText(number=0, text=u'For Help, press F1')
        parent.SetStatusText(number=5, text=u'NUM')
        parent.SetStatusText(number=6, text=u'')

        parent.SetStatusWidths([-1, 24, 24, 32, 32, 32, 24])

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.menuFile = wx.Menu(title=u'')

        self.menuEdit = wx.Menu(title='')

        self.menuMailbox = wx.Menu(title=u'')

        self.menuMessage = wx.Menu(title='')

        self.menuTransfer = wx.Menu(title='')

        self.menuSpecial = wx.Menu(title='')

        self.menuTools = wx.Menu(title='')

        self.menuWindow = wx.Menu(title='')

        self.menuHelp = wx.Menu(title='')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menuFile_Items(self.menuFile)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MDIParentFrame.__init__(self, id=wxID_WXMDIPARENTFRAME1, name='',
              parent=prnt, pos=wx.Point(133, 88), size=wx.Size(874, 605),
              style=wx.DEFAULT_FRAME_STYLE | wx.VSCROLL | wx.HSCROLL,
              title=u'Elvira - [Ray]')
        self._init_utils()
        self.SetMenuBar(self.menuBar1)
        self.SetAutoLayout(True)
        self.SetClientSize(wx.Size(866, 571))
        self.SetIcon(wx.Icon(u'icons/EudoraRes_254.ico',
              wx.BITMAP_TYPE_ICO))
        self.Bind(wx.EVT_SIZE, self.OnWxmdiparentframe1Size)

        self.sashLayoutWindow1 = wx.SashLayoutWindow(id=wxID_WXMDIPARENTFRAME1SASHLAYOUTWINDOW1,
              name='sashLayoutWindow1', parent=self, pos=wx.Point(0, 28),
              size=wx.Size(537, 272), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow1.SetOrientation(wx.LAYOUT_VERTICAL)
        self.sashLayoutWindow1.SetAlignment(wx.LAYOUT_LEFT)
        self.sashLayoutWindow1.SetSashVisible(wx.SASH_RIGHT, True)
        self.sashLayoutWindow1.SetDefaultSize(wx.Size(137, 272))
        self.sashLayoutWindow1.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashlayoutwindow1SashDragged,
              id=wxID_WXMDIPARENTFRAME1SASHLAYOUTWINDOW1)

        self.toolBar1 = wx.ToolBar(id=wxID_WXMDIPARENTFRAME1TOOLBAR1,
              name='toolBar1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(866, 28), style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        self.SetToolBar(self.toolBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_WXMDIPARENTFRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetFieldsCount(2)
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.notebook1 = wx.Notebook(id=wxID_WXMDIPARENTFRAME1NOTEBOOK1,
              name='notebook1', parent=self.sashLayoutWindow1, pos=wx.Point(0,
              0), size=wx.Size(534, 272), style=wx.NB_BOTTOM)

        self.treeCtrl1 = wx.TreeCtrl(id=wxID_WXMDIPARENTFRAME1TREECTRL1,
              name='treeCtrl1', parent=self.notebook1, pos=wx.Point(0, 0),
              size=wx.Size(526, 246), style=wx.TR_HAS_BUTTONS)

        self.treeCtrl2 = wx.TreeCtrl(id=wxID_WXMDIPARENTFRAME1TREECTRL2,
              name='treeCtrl2', parent=self.notebook1, pos=wx.Point(0, 0),
              size=wx.Size(526, 246), style=wx.TR_HAS_BUTTONS)

        self.listView1 = wx.ListView(id=wxID_WXMDIPARENTFRAME1LISTVIEW1,
              name='listView1', parent=self.notebook1, pos=wx.Point(0, 0),
              size=wx.Size(526, 246), style=wx.LC_ICON)

        self.listView2 = wx.ListView(id=wxID_WXMDIPARENTFRAME1LISTVIEW2,
              name='listView2', parent=self.notebook1, pos=wx.Point(0, 0),
              size=wx.Size(526, 246), style=wx.LC_ICON)

        self.listCtrl1 = wx.ListCtrl(id=wxID_WXMDIPARENTFRAME1LISTCTRL1,
              name='listCtrl1', parent=self.notebook1, pos=wx.Point(0, 0),
              size=wx.Size(526, 246), style=wx.LC_ICON)

        self._init_coll_toolBar1_Tools(self.toolBar1)
        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

        child1 = wxMDIChildFrame1.create(self)
        child1.Show(True)

    def OnMenuFileitems0Menu(self, event):
        wxMDIChildFrame1.create(self).Show(True)

    def OnWxmdiparentframe1Size(self, event):
        wx.LayoutAlgorithm().LayoutMDIFrame(self)

    def OnSashlayoutwindow1SashDragged(self, event):
        if event.GetDragStatus() == wx.SASH_STATUS_OUT_OF_RANGE:
            return

        eID = event.GetId()
        if eID == wxID_WXMDIPARENTFRAME1SASHLAYOUTWINDOW1:
            self.sashLayoutWindow1.SetDefaultSize(wx.Size(event.GetDragRect().width, 0))

        wx.LayoutAlgorithm().LayoutMDIFrame(self)
        self.GetClientWindow().Refresh()

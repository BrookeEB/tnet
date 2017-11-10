import wx

BACKGROUNDCOLOR = (240, 240, 240, 255)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.createWidgets()
        self.Show()

    def exitGUI(self, event):
        self.Destroy()

    def createWidgets(self):
        self.CreateStatusBar()
        self.CreateMenu()
        self.createNotebook()

    def CreateMenu(self):
        menu = wx.Menu()
        menu.Append(wx.ID_ABOUT, "About", "wxPythonGUI")

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "MENU")
        self.SetMenuBar(menuBar)

    def createNotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)
        notebook.AddPage(widgets, "Widgets")
        notebook.SetBackgroundColour(BACKGROUNDCOLOR)
        boxSizer = wx.BoxSizer()
        boxSizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizerAndFit(boxSizer)


class Widgets(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel = wx.Panel(self)
        self.createWidgetsFrame()
        self.createManageFilesFrame()
        self.addWidgets()
        self.addFileWidgets()
        self.layoutWidgets()
        self.path = None

    def createWidgetsFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, "Widgets Frame", size=(450, -1))
        self.statBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

    def layoutWidgets(self):
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(self.statBoxSizerV, 1, wx.ALL)
        boxSizerV.Add(self.statBoxSizerMgrV, 1, wx.ALL)
        self.panel.SetSizer(boxSizerV)
        boxSizerV.SetSizeHints(self.panel)

    def addWidgets(self):
        self.addStaticBoxWithLabels()

    def addFileWidgets(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self.panel, label='Open Data File...')
        btn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        boxSizerH.Add(btn)

        self.file_text = wx.TextCtrl(self.panel, size=(350, -1), value="Select A Data File")
        boxSizerH.Add(self.file_text)

        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(boxSizerH)
        self.statBoxSizerMgrV.Add(boxSizerV, 1, wx.ALL)

    def addStaticBoxWithLabels(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        staticBox = wx.StaticBox(self.panel, -1, "Labels within a Frame")
        staticBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        staticText1 = wx.StaticText(self.panel, -1, "Choose a number:")
        boxSizerV.Add(staticText1, 0, wx.ALL)
        staticText2 = wx.StaticText(self.panel, -1, "Label 2")
        boxSizerV.Add(staticText2, 0, wx.ALL)
        staticBoxSizerV.Add(boxSizerV, 0, wx.ALL)
        boxSizerH.Add(staticBoxSizerV)
        boxSizerH.Add(wx.TextCtrl(self.panel))
        self.statBoxSizerV.Add(boxSizerH, 1, wx.ALL)

    def createManageFilesFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, "Manage Files", size=(450, -1))
        self.statBoxSizerMgrV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

    def onOpenFile(self, event):
        """
        Create and show the Open FileDialog
        """
        wildcard = "tNet Data (*.csv)|*.csv|" \
                   "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="File",
            defaultFile="",
            wildcard=wildcard,
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            self.path = paths[0]
            self.file_text.SetValue(paths[0])
        dlg.Destroy()
















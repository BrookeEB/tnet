import wx
import networkx as nx

from jumps import build_network

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
        menu.Append(wx.ID_ABOUT, "About", "tNet 0.1")

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

    def createNotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)
        notebook.AddPage(widgets, "tNet")
        notebook.SetBackgroundColour(BACKGROUNDCOLOR)
        boxSizer = wx.BoxSizer()
        boxSizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizerAndFit(boxSizer)


class Widgets(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel = wx.Panel(self)

        self.create_widget_frame()
        self.add_mission_widgets()
        self.layout_widgets()
        self.path = None

    def create_widget_frame(self):
        staticBox = wx.StaticBox(self.panel, -1,
                                 "Transportation Network",
                                 size=(350, -1))
        self.statBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

    def layout_widgets(self):
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(self.statBoxSizerV, 1, wx.ALL)
        self.panel.SetSizer(boxSizerV)
        boxSizerV.SetSizeHints(self.panel)

    def add_mission_widgets(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self.panel, label='Open Data File...')
        btn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        boxSizerH.Add(btn)
        self.file_text = wx.TextCtrl(self.panel, size=(350, -1))
        boxSizerH.Add(self.file_text)
        self.statBoxSizerV.Add(boxSizerH, 1, wx.ALL)

        self.start = wx.ComboBox(self.panel, -1, "Select Start",
                            choices=['Open A Data File'], size=(120, -1))
        self.stop = wx.ComboBox(self.panel, -1, "Select Target",
                           choices=['Open A Data File'], size=(120, -1))
        self.statBoxSizerV.Add(self.start)
        self.statBoxSizerV.Add(self.stop)

        self.fspeed = wx.Slider(self.panel, value=10, minValue=4, maxValue=30,
                                style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.statBoxSizerV.Add(wx.StaticText(self.panel,
                                             label='Set Fleet Speed',
                                             style=wx.ALIGN_CENTER),
                               1,
                               wx.ALIGN_CENTRE_HORIZONTAL)
        self.statBoxSizerV.Add(self.fspeed,
                               1,
                               flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.TOP
                               )

        button = wx.Button(self.panel, id=wx.ID_ANY, label="Solve")
        button.Bind(wx.EVT_BUTTON, self.solve)
        self.statBoxSizerV.Add(button)

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
            self.build_network()
            nodes = list(nx.nodes(self.network))
            nodes.sort()
            self.start.SetItems(nodes)
            self.stop.SetItems(nodes)
        dlg.Destroy()

    def build_network(self):
        self.network = build_network(self.path, self.fspeed.GetValue())

    def solve(self, event):
        self.build_network()
        solution = nx.dijkstra_path(self.network,
                                    self.start.GetValue(),
                                    self.stop.GetValue())
        flight_time = nx.dijkstra_path_length(self.network,
                                              self.start.GetValue(),
                                              self.stop.GetValue())
        direct = self.network.get_edge_data(self.start.GetValue(),
                                            self.stop.GetValue())['weight']
        message = f'{solution}-{flight_time} minutes vs {direct} minutes direct'
        wx.MessageBox(message,
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)

from wx import App
from gui import MainFrame

app = App()
MainFrame(None, size=(500, 300))
app.MainLoop()
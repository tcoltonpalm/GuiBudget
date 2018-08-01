import wx
from wx.lib.masked.numctrl import NumCtrl
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
        self.createnotebook()

    def CreateMenu(self):
        menu = wx.Menu()
        menu.Append(wx.ID_ABOUT, "About", "Personal Budget")

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

    def createnotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)
        notebook.AddPage(widgets, "Personal Budget")
        notebook.SetBackgroundColour(BACKGROUNDCOLOR)
        boxSizer = wx.BoxSizer()
        boxSizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizerAndFit(boxSizer)


class Widgets(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel = wx.Panel(self)

        self.make_widget_frame()
        self.add_working_widgets()
        self.layout_widgets()
        self.path = None

    def make_widget_frame(self):
        staticBox = wx.StaticBox(self.panel, -1,
                                 "Budget",
                                 size=(350, -1))
        self.statBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

    def layout_widgets(self):
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(self.statBoxSizerV, 1, wx.ALL)
        self.panel.SetSizer(boxSizerV)
        boxSizerV.SetSizeHints(self.panel)

    def add_working_widgets(self):
        boxSizerH_titles = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        # btn = wx.Button(self.panel, label='Income')


       # boxSizerH = wx.Button(self.panel, lable='Gas')
       #  boxSizerH.Add(btn)

        title = wx.StaticText(self, label="{:^18}".format("Budget"))
        self.budget = NumCtrl(self.panel, value=0)
        title2 = wx.StaticText(self, label="{:^18}".format("Food"))
        self.food = NumCtrl(self.panel, value=0)
        title3 = wx.StaticText(self, label="{:^18}".format("Car"))
        self.car = NumCtrl(self.panel, value=0)
        title4 = wx.StaticText(self, label="{:^20}".format("Utilities"))
        self.utilities = NumCtrl(self.panel, value=0)

        boxSizerH.Add(self.budget)
        boxSizerH_titles.Add(title)
        boxSizerH.Add(self.food)
        boxSizerH_titles.Add(title2)
        boxSizerH.Add(self.car)
        boxSizerH_titles.Add(title3)
        boxSizerH.Add(self.utilities)
        boxSizerH_titles.Add(title4)

        self.statBoxSizerV.Add(boxSizerH_titles, 1, wx.ALL)
        self.statBoxSizerV.Add(boxSizerH, 1, wx.ALL)


        self.statBoxSizerV.AddSpacer(2)

        self.statBoxSizerV.AddSpacer(2)

        self.statBoxSizerV.Add(wx.StaticText(self.panel,
                                             label='Expense',
                                             style=wx.ALIGN_CENTER),
                               1,
                               wx.ALIGN_CENTRE_HORIZONTAL)

        solve_button = wx.Button(self.panel, id=wx.ID_ANY, label="Run the Numbers")
        solve_button.Bind(wx.EVT_BUTTON, self.show_numbers)
        self.statBoxSizerV.Add(solve_button, 0, wx.CENTER)
        percents_button = wx.Button(self.panel, id=wx.ID_ANY, label="Percentages")
        percents_button.Bind(wx.EVT_BUTTON, self.show_percentages)
        self.statBoxSizerV.Add(percents_button, 0, wx.CENTER)


    def show_numbers(self, event):
        total = self.budget.GetValue() - ( self.food.GetValue() + self.car.GetValue() + self.utilities.GetValue() )

        wx.MessageBox("Money: {}".format(total),
                      'Budget Results',
                      wx.OK | wx.ICON_INFORMATION)

    def show_percentages(self, event):
        totalPercent = ((self.food.GetValue() / self.budget.GetValue()*100)  ,  (self.car.GetValue() /self.budget.GetValue()*100),  (self.utilities.GetValue()/ self.budget.GetValue())*100)

        wx.MessageBox("Percent: {}".format(totalPercent),
                      'Percentage Results',
                      wx.OK | wx.ICON_INFORMATION)
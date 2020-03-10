import wx
from login import LoginSystem
import dbConnection


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame,self).__init__(parent, title=title, size=(400, 400))

        # create panel inside frame
        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        self.label = wx.StaticText(self, label='Username', pos=(100,150))
        self.usernameInput = wx.TextCtrl(self, pos=(180, 150))
        self.label = wx.StaticText(self, label='Password', pos=(100, 180))
        self.passwordInput = wx.TextCtrl(self, style=wx.TE_PASSWORD, pos=(180, 180))
        self.loginBtn = wx.Button(self, label='Login', pos=(180, 220))
        self.loginBtn.Bind(wx.EVT_BUTTON, self.OnLoginClick)

    def OnLoginClick(self, event):
        print(self.usernameInput.GetValue(), self.passwordInput.GetValue())
        user = LoginSystem()
        authorized = user.login(self.usernameInput.GetValue(), self.passwordInput.GetValue())
        if authorized:
            wx.MessageBox('Login Successful', 'Success!', wx.OK| wx.ICON_INFORMATION)
        else:
            wx.MessageBox('Invalid Credentials', 'Error!', wx.OK | wx.ICON_INFORMATION)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title='Login')
        self.frame.Show()

        return True


app = MyApp()
app.MainLoop()
dbConnection.closeDB()



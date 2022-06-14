from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window
from screens.screens import *

#Window Size
Window.size = (350,600)

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [
            Welcome(name='welcome'),
            Login(name='login'),
            Signup(name='signup'),
        ]

        for screen in screens:
            self.wm.add_widget(screen)


        return self.wm


if __name__ == '__main__':
    LabelBase.register(name="MAIAN", fn_regular="assets/fonts/MAIAN.TTF")
    LabelBase.register(name="PrestigeB", fn_regular="assets/fonts/PrestigeEliteStd-Bd.otf")
    MainApp().run()
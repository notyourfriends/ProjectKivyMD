from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

from screens.screens import *

class WindowManager(ScreenManager):
    pass



class MainApp(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [
            Welcome(name='welcome')
        ]

        for screen in screens:
            self.wm.add_widget(screen)


        return self.wm


if __name__ == '__main__':
    LabelBase.register(name="MAIAN", fn_regular="assets/fonts/MAIAN.TTF")
    MainApp().run()
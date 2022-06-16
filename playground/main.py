#from kaki.app import App
from kivymd.tools.hotreload.app import MDApp
#from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window

from screens.screens import *

Window.size = (350, 660)

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    CLASSES = {
        #Name class : location
        'Welcome':'screens.welcome',
        'Login':'screens.login',
        'Signup':'screens.signup',
    }
    AUTORELOADER_PATHS = [

        ('.',{'recursive':True}),
    ]
    KV_FILES = [
        'kv/welcome.kv',
        'kv/login.kv',
        'kv/signup.kv',
    ]

    def build_app(self):
        self.wm = WindowManager()
        screens = [
            Welcome(name="welcome"),
            Login(name="login"),
            Signup(name="signup"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__':
    LabelBase.register(name="MAIAN", fn_regular="assets/fonts/MAIAN.TTF")
    LabelBase.register(name="PrestigeB", fn_regular="assets/fonts/PrestigeEliteStd-Bd.otf")
    MainApp().run()
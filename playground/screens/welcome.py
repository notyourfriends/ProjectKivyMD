from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#from kivy.factory import Factory as F

class Welcome(MDScreen):
    def __init__(self, **kw):
        Builder.load_file('kv/welcome.kv')
        super().__init__(**kw)

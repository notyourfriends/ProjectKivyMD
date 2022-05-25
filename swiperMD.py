from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
	dialog = None
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('swiperMD.kv')
	
MainApp().run()
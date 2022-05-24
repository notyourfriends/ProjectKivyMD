from kivymd.app import MDApp
from kivy.lang import Builder

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'Blue'
		return Builder.load_file('test.kv')

MainApp().run()
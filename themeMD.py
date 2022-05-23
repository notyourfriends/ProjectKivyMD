from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Green"
		self.theme_cls.accent_palette = "Teal"
		return Builder.load_file('themeMD.kv')

#Red, Pink, Purple, DeepPurple
#Indigo, Blue, LightBlue, Cyan
#Teal, Green, LightGreen, Lime
#Yellow, Amber, Orange, DeepOrange
#Brown, Gray, BlueGray

MainApp().run()
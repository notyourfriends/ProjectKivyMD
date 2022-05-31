from kivy.config import Config
#Config.set('graphics', 'position', 'custom') set pos
#Config.set('graphics', 'left', '100')
#Config.set('graphics', 'top', '100')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


class DateApp(MDApp):
	def build(self):
		Window.borderless = True
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('notitlebar.kv')

	def stop(self):
		pass



DateApp().run()
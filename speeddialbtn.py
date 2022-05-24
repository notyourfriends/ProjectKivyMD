from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):

	data = {
		"Python" :  "language-python",
		"Ruby" :  "language-ruby" ,
		"JS" : "language-javascript"
	}

	def callback(self, instance):
		if instance.icon == 'language-python':
			lang = 'Python'
		elif instance.icon == 'language-javascript':
			lang = "JS"
		elif instance.icon == 'language-ruby':
			lang = 'Ruby'
		self.root.ids.my_label.text = f'You press {lang}'

	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('speeddialbtn.kv')
	

MainApp().run()
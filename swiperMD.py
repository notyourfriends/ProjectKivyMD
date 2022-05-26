from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
	dialog = None
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('swiperMD.kv')

	def get_previous(self):
		if self.root.ids.swiper.get_current_index() > 0: 
			self.root.ids.swiper.set_current(self.root.ids.swiper.get_current_index()-1)

	def get_next(self):
		if self.root.ids.swiper.get_current_index() < len(self.root.ids.swiper.get_items())-1: 
			self.root.ids.swiper.set_current(self.root.ids.swiper.get_current_index()+1)

	def on_swipe_left(self):
		self.root.ids.toolbar.title = "Swiped to Previous Image"
		print("Swiped to previous Image")
	
	def on_swipe_right(self):
		self.root.ids.toolbar.title = "Swiperd to Next Image"
		print("Swiped to next Image")
MainApp().run()
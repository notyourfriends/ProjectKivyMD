from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

#pip install kivy_garden
#garden install matplotlib


#Define what we want to graph
x = [1,2,3,4,5]
y = [5, 2, 6, 12, 9]

plt.plot(x,y)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")

class Matty(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		box = self.ids.box
		box.add_widget(FigureCanvasKivyAgg(plt.gcf())) #GCF = Get Current Figure

	def save(self):
		pass

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		Builder.load_file("mathlib.kv")
		return Matty()

MainApp().run()
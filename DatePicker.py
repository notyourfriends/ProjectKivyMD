from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDDatePicker

class DateApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('datepicker.kv')

	# clicked OK
	def on_save(self, instance, value, date_range):
		#print(instance, value, date_range)
		self.root.ids.date_label.text = str(value)
		
		#showing range date
		#self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'
	# clicked Cancel	
	def on_cancel(self, instance, value):
		self.root.ids.date_label.text = "You clicked Cancel"

	def show_date_picker(self):
		#date_dialog = MDDatePicker(year = 1999, month= 9, day = 5) #set date
		#date_dialog = MDDatePicker() #current date
		date_dialog = MDDatePicker(mode ="range") #current date

		date_dialog.bind(on_save = self.on_save, on_cancel = self.on_cancel)
		date_dialog.open()

DateApp().run()
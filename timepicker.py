from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDTimePicker

class DateApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('timepicker.kv')

	#Get Time
	def get_time(self, instance, time):
		self.root.ids.time_label.text = str(time)


	#Cancel
	def on_cancel(self, instance, time):
		self.root.ids.time_label.text = 'Pressed Cancel'

	def show_time_picker(self):
		from datetime import datetime

		#Define default time
		default_time = datetime.strptime("04:20:00", '%H:%M:%S').time()


		time_dialog = MDTimePicker()
		#when you need to set default time
		time_dialog.set_time(default_time)


		time_dialog.bind(on_cancel = self.on_cancel, time=self.get_time)
		time_dialog.open()

DateApp().run()
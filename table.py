from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp #Display Pixles

class MainApp(MDApp):
	def build(self):
		#Define Screen
		screen = Screen()
		#Define table
		table = MDDataTable(
			pos_hint = {'center_x': .5, 'center_y': .5},
			size_hint = (0.9, 0.6),
			check = True,
			use_pagination = True,
			rows_num = 3, 
			pagination_menu_height = '240dp',
			pagination_menu_pos = 'auto', #doesn't work
			background_color = [1,0,0,.5], #doesn't work

			column_data = [
				('First Name', dp(30)),
				('Last Name', dp(30)),
				('Email Address', dp(50)),
				('Phone Number', dp(30)),
			],
			row_data = [
				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				('Muhamad Refo', 'Alpha Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

				(' Refo', ' Rizky', 'refo.alpha@gmail.com', '081255667780'),
				('Fuu', 'Nii', 'fuunii99@gmail.com', '085719328218'),

			]

			)
		#Bind Table
		table.bind(on_check_press = self.checked)
		table.bind(on_row_press = self.row_checked)



		self.theme_cls.theme_style = 'Light'
		self.theme_cls.primary_palette = 'BlueGray'
		#return Builder.load_file('table.kv')

		#add Table widget to screen
		screen.add_widget(table)
		return screen

	def checked(self, instance_table, current_row):
		print(instance_table, current_row)
	def row_checked(self,instance_table, instance_row):
		print(instance_table, instance_row)

MainApp().run()
from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    title = "List with KivyMD"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette ="BlueGray"
        return Builder.load_file("listMD.kv")

    def presser(self, pressed, list_id):
        pressed.text = f"You Pressed {list_id}"
        pressed.secondary_text = f"You Pressed {list_id}"
        pressed.tertiary_text = f"You Pressed {list_id}"


MainApp().run()
from kivy.factory import Factory as F
from kivy.lang import Builder

Builder.load_string("""
<UI>:
    cols: 1
    Label:
        text: str(slider.value)
    Slider:
        id: slider
    ToggleButton:
        id: btn
        text:'text'
""")

class UI(F.GridLayout):
    pass
#from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer

#pip install ffpyplayer

class MainApp(MDApp):
    title = "Video Player with KivyMD"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette ="BlueGray"
        #return Builder.load_file("VidPlayer.kv")

        #Create videoPlayer Instance
        player = VideoPlayer(source ="D:\Download\Video\ネクライトーキーMV「北上のススメ」.mp4" )

        # Assign VideoPlayer State
        player.state = 'play'
        #Set options
        player.options = {'eos': 'loop'} 
        #Allow stretch
        player.allow_stretch = True

        return player

MainApp().run()
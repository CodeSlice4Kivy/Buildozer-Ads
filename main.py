from kivy.app import App
from kivmob import KivMob, TestIds
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

ads = KivMob('ca-app-pub-3940256099942544/3419835294')

class Home(Screen):

    def on_pre_enter(self,*args):
        ads.new_banner('ca-app-pub-3940256099942544/6300978111',top_pos=False)
        ads.request_banner()
        ads.show_banner()

class MainApp(App):
    def build(self):
        return Home()

MainApp().run()



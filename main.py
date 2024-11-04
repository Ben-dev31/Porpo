
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp


Builder.load_file("layouts/main_layout.kv")

class MainScreen(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class CalculatorApp(MDApp):
    def build(self):
        return MainScreen()

CalculatorApp().run()

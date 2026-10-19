from kivy.app import App
from kivy.uix.label import Label

class Jarvis(App):
    def build(self):
        return Label(text="Jarvis ready")

Jarvis().run()

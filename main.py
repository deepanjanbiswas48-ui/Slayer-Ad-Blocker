from kivy.app import App
from kivy.uix.label import Label

class SlayerApp(App):
    def build(self):
        return Label(text='Slayer Ad-Blocker Running!')

if __name__ == '__main__':
    SlayerApp().run()

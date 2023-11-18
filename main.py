from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Devmoney(MDApp):
    def build(self):
        return MDLabel(text="Hello, Devmoney", halign="center")


Devmoney().run()
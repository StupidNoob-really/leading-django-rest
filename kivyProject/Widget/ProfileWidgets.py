from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MainLayout(BoxLayout):
    orientation = 'vertical'
    padding = [20, 20, 20, 20]



class SpaceLayout(BoxLayout):
    pass


class TitleLabel(Label):
    text = 'Title'
    color = (.9, .9, .9, 1)
    halign = 'left'
    valign = 'bottom'


class ValueLabel(Label):
    text = 'Value'
    color = (.9, .9, .9, 1)
    halign = 'left'
    valign = 'bottom'


class FieldLayout(BoxLayout):
    orientation = 'horizontal'
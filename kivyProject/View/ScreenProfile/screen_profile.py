from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from Utility.observer import Observer
from Widget import ProfileWidgets as pw

from kivy.network.urlrequest import UrlRequest


class ProfileView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    screen_managers = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.main_layout = pw.MainLayout()
        self.model.add_observer(self)

    def on_pre_enter(self):
        label = pw.TitleLabel(text='Request')
        self.main_layout.add_widget(label)
        self.add_widget(self.main_layout)

    def on_enter(self):
        label = self.main_layout.children[0]
        label.text = '123'

    def model_is_changed(self):
        pass
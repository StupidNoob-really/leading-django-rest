from kivy.properties import ObjectProperty
from kivymd.uix.screen import Screen
from Widget import LoginWidgets

from Utility.observer import Observer


class LoginView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def to_screen_profile(self, instance):
        self.manager_screens.current = 'ScreenProfile'

    def on_enter(self, *args):
        button = LoginWidgets.login_button()
        button.bind(on_press=self.to_screen_profile)

        main_layout = LoginWidgets.main_layout()
        form_layout = LoginWidgets.form_layout()

        form_layout.add_widget(LoginWidgets.space_layout())
        form_layout.add_widget(LoginWidgets.error_label())
        form_layout.add_widget(LoginWidgets.login_input())
        form_layout.add_widget(LoginWidgets.password_input())
        form_layout.add_widget(button)
        form_layout.add_widget(LoginWidgets.space_layout())

        main_layout.add_widget(form_layout)
        self.add_widget(main_layout)

    def model_is_changed(self):
        pass
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition
from View.screens import screens


class TextMVC(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = ScreenManager(transition=NoTransition())

    def build(self):
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self):
        """
        Создание и добавление экранов в диспетчер экранов.
        Вы не должны изменять этот цикл без необходимости. Он самодостаточен.

        Если вам нужно добавить какой-либо экран, откройте модуль View.screens.py и
        посмотреть, как добавляются новые экраны в соответствии с данным приложением
        архитектура.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


TextMVC().run()

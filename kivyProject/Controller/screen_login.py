from View.ScreenLogin.screen_login import LoginView


class LoginController:
    def __init__(self, model):
        self.model = model
        self.view = LoginView(controller=self, model=model)

    def get_view(self) -> LoginView:
        return self.view
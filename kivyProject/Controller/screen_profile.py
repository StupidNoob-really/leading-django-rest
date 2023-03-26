from View.ScreenProfile.screen_profile import ProfileView


class ProfileController:
    def __init__(self, model):
        self.model = model
        self.view = ProfileView(controller=self, model=self.model)

    def get_view(self):
        return self.view
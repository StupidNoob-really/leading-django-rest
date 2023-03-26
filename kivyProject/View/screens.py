from Controller.screen_login import LoginController
from Model.screen_login import LoginModel
from Controller.screen_profile import ProfileController
from Model.screen_profile import ProfileModel

screens = {
    'ScreenLogin': {
        'controller': LoginController,
        'model': LoginModel,
    },
    'ScreenProfile': {
        'controller': ProfileController,
        'model': ProfileModel,
    }
}

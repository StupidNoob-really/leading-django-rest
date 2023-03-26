from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


size_hint_form = (.7, 1)
size_hint_form_children = (1, .2)


def main_layout() -> AnchorLayout:
    widget = AnchorLayout()
    return widget


def form_layout() -> BoxLayout:
    widget = BoxLayout()
    widget.size_hint = size_hint_form
    widget.orientation = 'vertical'
    return widget


def login_input() -> TextInput:
    widget = TextInput()
    widget.size_hint = size_hint_form_children
    widget.multiline = False
    widget.hint_text = 'Логин'
    return widget


def password_input() -> TextInput:
    widget = TextInput()
    widget.size_hint = size_hint_form_children
    widget.multiline = False
    widget.password = True
    widget.hint_text = 'Пароль'
    return widget


def error_label() -> Label:
    widget = Label()
    widget.size_hint = size_hint_form_children
    widget.halign = 'left'
    widget.valign = 'bottom'
    widget.bind(size=widget.setter('text_size'))
    widget.color = (1, .2, .2, 1)
    return widget


def space_layout() -> BoxLayout:
    widget = BoxLayout()
    return widget


def login_button() -> Button:
    widget = Button()
    widget.size_hint = size_hint_form_children
    widget.text = 'Авторизироваться'
    return widget
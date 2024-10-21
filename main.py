import kivy

kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox

class Forms(App):
    def build(self):
        return FormLayout()
#    def submit_form(self):
 #       product_name = self.root.ids.product_name_input.text:

class FormLayout(BoxLayout):
    pass

if __name__ == '__main__':
   Forms().run()
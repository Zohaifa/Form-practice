import kivy
import re

kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

class Forms(App):
    def build(self):
        return MyForm()


class MyForm(BoxLayout):
    def __init__(self, **kwargs):
        super(MyForm, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.name_input = TextInput(hint_text = 'Enter your name here')
        self.add_widget(self.name_input)

        self.price_input = TextInput(hint_text = 'Enter Price here', input_filter = 'float')
        self.add_widget(self.price_input)

        self.email_input = TextInput(hint_text = 'Enter your E-mail')
        self.add_widget(self.email_input)

        self.submit_btn = Button(text = "Submit", on_press = self.submit_form)
        self.add_widget(self.submit_btn)

        self.error_label = Label(color = (1,0,0,1))
        self.add_widget(self.error_label)

    def validate_text_input(self, input_field):
        if input_field.text.strip() == "":
            input_field.background_color = (1, 0, 0, 1)
            return False, "This field cannot be empty"
        input_field.background_color = (1, 1, 1, 1)
        return True, ""
    def validate_numeric_input(self, input_field):
        try:
            value = float(input_field.text)
            if value < 0:
                return False, "Value cannot be negative"
            return True, ""
        except ValueError:
            return False, "Please enter a valid number"
    def validate_email_address(self, input_field):
        pattern = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, input_field.text):
            return False, "Please enter a valid email address"
        return True, ""
    def submit_form(self, instance):
        valid_name, name_error = self.validate_text_input(self.name_input)
        valid_price, price_error = self.validate_numeric_input(self.price_input)
        valid_email, email_error = self.validate_email_address(self.email_input)

        if not (valid_name and valid_price and valid_email):
            self.display_error([name_error, price_error, email_error])
        else:
            self.error_label.color = (1, 1, 1, 1)
            self.error_label.text = "Form Submitted successfully"

    def display_error(self, errors):
        error_messages = "\n".join([error for error in errors if error])
        self.error_label.text = error_messages


if __name__ == '__main__':
   Forms().run()
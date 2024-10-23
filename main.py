import kivy
import re

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
    def validate_text_input(self, input_field):
        if input_field.text.strip() == "":
        #    input_field.background_color = (1, 0, 0, 1)
            return False, "This field cannot be empty"
        #input_field.background_color = (1, 1, 1, 1)
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
    def submit_form(self):
        product_name = self.root.ids.product_name_input.text
        price = self.root.ids.price_input.text
        category = self.root.ids.category_spinner.text
        checkbox = self.root.ids.in_stock_checkbox.active

        print(f"Product Name: {product_name}")
        print(f"Price: {price}")
        print(f"Category: {category}")
        print(f"In Stock: {checkbox}")

class FormLayout(BoxLayout):
    pass

if __name__ == '__main__':
   Forms().run()
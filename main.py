import kivy
import re
import json

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

        self.twobuttons = BoxLayout(orientation = 'horizontal')
        self.show_from_file = Button(text = "Show from Textfile", on_press = self.display_data_from_file)
        self.twobuttons.add_widget(self.show_from_file)
        self.show_from_json = Button(text = "Show from Json file", on_press = self.display_data_from_json)
        self.twobuttons.add_widget(self.show_from_json)

        self.add_widget(self.twobuttons)

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

            form_data = {
                "name" : self.name_input.text,
                "price" : self.price_input.text,
                "email" : self.email_input.text
            }
            self.display_data(form_data)
            self.save_data_to_file(form_data)
            self.save_data_to_json(form_data)
            self.clear_form()

    def clear_form(self):
        self.name_input.text = ""
        self.price_input.text = ""
        self.email_input.text = ""

    def display_data(self, form_data):
        self.error_label.text = f"Name: {form_data['name']}\nPrice: {form_data['price']}\nEmail:{form_data['email']}\n"

    def display_error(self, errors):
        error_messages = "\n".join([error for error in errors if error])
        self.error_label.text = error_messages

    def save_data_to_file(self, form_data):
        with open('form_data.txt', 'a') as file:
            file.write(f"Name: {form_data['name']}, Price: {form_data['price']}, Email: {form_data['email']}\n")

    def save_data_to_json(self, form_data):
        try:
            with open("form_data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.append(form_data)
        with open("form_data.json", 'w') as file:
            json.dump(data, file, indent=4)

    def display_data_from_file(self, instance):
        try:
            with open('form_data.txt', 'r') as file:
                data = file.read()
            self.error_label.text = data
        except FileNotFoundError:
            self.error_label.text = "No data available"

    def display_data_from_json(self, instance):
        try:
            with open('form_data.json', 'r') as file:
                data = json.load(file)
            display_text = "\n".join([f"Name: {item['name']}, Price: {item['price']}, Email: {item['email']}" for item in data])
            self.error_label.text = display_text
        except FileNotFoundError:
            self.error_label.text = "No data available"

if __name__ == '__main__':
   Forms().run()
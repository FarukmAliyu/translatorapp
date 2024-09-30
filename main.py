# Import necessary libraries
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner  # For language selection
from googletrans import Translator, LANGUAGES

class TranslatorApp(App):

    def build(self):
        # Initialize translator
        self.translator = Translator()

        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=(10, 10))

        # Create input and output text fields
        self.input_text = TextInput(hint_text='Enter text to translate', multiline=True, font_size=16)
        self.output_text = TextInput(hint_text='Translation', multiline=True, readonly=True, font_size=16)

        # Create a language selector using Spinner
        self.language_spinner = Spinner(
            text='Select language',  # Default value of the spinner
            values=list(LANGUAGES.values()),  # Get list of languages from googletrans
            size_hint=(None, None),
            size=(200, 50)
        )

        # Create a translate button
        translate_button = Button(text='Translate', on_press=self.translate_text, size_hint=(None, None))
        translate_button.size = (150, 50)

        # Add widgets to the layout
        layout.add_widget(Label(text="Select target language:"))
        layout.add_widget(self.language_spinner)
        layout.add_widget(Label(text="Enter text to translate:"))
        layout.add_widget(self.input_text)
        layout.add_widget(Label(text="Translated text:"))
        layout.add_widget(self.output_text)
        layout.add_widget(translate_button)

        return layout

    def translate_text(self, instance):
        # Get the input text
        input_text = self.input_text.text

        # Get the selected language code from the spinner
        target_language = self.language_spinner.text
        if target_language == 'Select language':
            self.output_text.text = 'Please select a language'
            return

        # Get the corresponding language code from the LANGUAGES dictionary
        target_lang_code = [code for code, lang in LANGUAGES.items() if lang == target_language][0]

        # Check if the input text is not empty
        if input_text:
            try:
                # Translate the text using the Google Translate API
                translation = self.translator.translate(input_text, dest=target_lang_code).text

                # Display the translation in the output text field
                self.output_text.text = translation
            except Exception as e:
                self.output_text.text = f"Error: {e}"
        else:
            # If the input text is empty, display a message in the output field
            self.output_text.text = 'Please enter text to translate'

if __name__ == '__main__':
    TranslatorApp().run()

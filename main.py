from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pyttsx3

engine = pyttsx3.init()

class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.name = TextInput(hint_text='What you want to speak, write here :',size_hint=(.5,.1),multiline=False)
        self.add_widget(self.name)
        self.submit = Button(text="Speak", size_hint=(.1,.1), background_color=(15,210,51),pos=(300,350))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def speak(self,texts):
        engine.say(texts)
        engine.runAndWait()

    def pressed(self, instance):
        self.speak(self.name.text)
        self.name.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
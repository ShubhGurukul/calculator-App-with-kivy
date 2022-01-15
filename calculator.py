from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# Window.clearcolor = .3, .3, .3, 1


class Calculator(BoxLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
    def on_enter(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"



class MenuScreen(Screen):
    pass


class CalculatorScreen(Screen, Calculator):
    pass


class ScreenManagement(ScreenManager):
    pass


# Builder.load_file("screen_with_calc.kv")


class MyCalculatorApp(App):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    MyCalculatorApp().run()

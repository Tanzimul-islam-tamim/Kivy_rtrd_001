import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.popup import Popup

import os

class FloatLayoutt(FloatLayout):
    pass


#Main Window Class and Function-                                       NEVER PUT ID OF .KV WITHIN QUOTE S ""


class MainWindow(Screen):
    def fltt(self):
        flt = FloatLayoutt()

#Main Window Class and Function\

#Second Window Class and Function-
class SecondWindow(Screen):
    def fltt(self):
        flt = FloatLayoutt()
        clr = Color()

    def Popss(self):
        sb = SubmitPop()


#Third Window Class and Function-
class ThirdWindow(Screen):
    def fltt(self):
        flt = FloatLayoutt()
        Wimg = Image()

#Third Window Class and function\
class SubmitAssurance(Screen):
    pass

def SubmitPop():
    Fpops = FloatLayoutt()
    Pop =  Popup(title="Congrats! Retard", content=Fpops,size_hint=(None,None), size = (300,300))
    Pop.open()






class Screenmngr(ScreenManager):
    pass

kv = Builder.load_file("spaceretard.kv")
sm = Screenmngr()
Screens = [MainWindow(name="main"),SecondWindow(name="Second"),ThirdWindow(name="Third")]

for scrn in Screens:
    sm.add_widget(scrn)







class MyApp(App):
    def build(self):
        return sm
if __name__ == "__main__":
    MyApp().run()
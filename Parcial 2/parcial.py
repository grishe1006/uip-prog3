#!/usr/bin/python
# -*- coding: 850 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuScreen(Screen):
	pass

class ResultadoScreen(Screen):
	pass


class ParcialApp(App):
	def build(self):
		pantalla = ScreenManager()
		pantalla.add_widget(MenuScreen(name = 'menu'))
		pantalla.add_widget(ResultadoScreen(name = 'resultado'))
		return pantalla

if __name__ == '__main__':
	ParcialApp().run()
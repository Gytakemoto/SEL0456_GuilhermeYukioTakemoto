#!/usr/bin/python

#Importa a biblioteca gráfica
import gi

#Seleciona a versão da biblioteca
gi.require_version("Gtk", "3.0")

#Importa o módulo gtk
from gi.repository import Gtk

# Criar uma nova classe descendente da classe Gtk.Window
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

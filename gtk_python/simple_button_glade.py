import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        fulano = builder.get_object("nome")
        print(f"Olá {fulano.get_text()}")


builder = Gtk.Builder()
builder.add_from_file("teste1.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()

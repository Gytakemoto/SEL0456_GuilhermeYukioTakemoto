import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

unit_store = Gtk.ListStore(int, str)

unit_store.append("Distância")
unit_store.append("Comprimento")

name_combo = Gtk.ComboBox.new_with_model_and_entry(unit_store)
name_combo.connect("changed", self.on_name_combo_changed)
name_combo.set_entry_text_column(1)
vbox.pack_start(name_combo, False, False, 0)


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        fulano = builder.get_object("nome")
        print(f"Olá {fulano.get_text()}")

    def onComboBox1(self, combo):
        


builder = Gtk.Builder()
builder.add_from_file("trabalho_final.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()

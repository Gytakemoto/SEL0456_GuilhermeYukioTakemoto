import gi
import pandas as pd
import numpy as np

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from os.path import abspath, dirname, join

def ReadExcel():

	Data = lambda:0												#Auxiliary struct

	#Reading the excel file
	data = pd.read_excel("trabalho_final.xls")      			#Reading the .xlsx file

	Properties_Units = data.iloc[0:0:,0::2]         			#Getting the headers

	Properties = list(Properties_Units)             			#Getting a list of the avaible properties
	Data.Properties = np.array(Properties)[:, None]      		#Transposing the list by transforming it into an 1D array

	Units = data.iloc[0::1,::2]                     			#Getting the Units from excel
	Data.Units = Units.values.tolist()                   		#Connverting them to a list

	factors = data.iloc[0::1,1::2]                  			#Getting the factors from excel
	Data.factors = factors.values.tolist()               		#Converting them to a list

	return Data

def UnitComboBox_Callback(self, Data):				#Callback when a Property is changed for in combo box
	aux = []

	#Removing previous lists
	self.liststore_Unit.clear()

	for Unit in range(len(Data.Units)):
		aux.append(Data.Units[Unit][self.active-1])					#Selecting desired units
		if str(aux[0]) != "nan":									#Removing excess cells
			self.liststore_Unit.append(aux)
		else:
			print("nan identificado, pulando...")
		aux = []
	
	#Cleaning previous stored combo lists and setting the current unit list
	self.combo_Unit.clear()
	self.combo_Unit.set_model(self.liststore_Unit)

Data = ReadExcel()

class TheApp:

		def __init__(self):
				# Build GUI
				self.builder = Gtk.Builder()
				self.builder.add_from_file('trabalho_final.glade')

				# Get objects
				self.window = self.builder.get_object('window')

				self.liststore = Gtk.ListStore(str)					#Combo Property identifier
				self.liststore_Unit = Gtk.ListStore(str)		#Combo Unit out identifier
				
				# Initialize interface
				self.liststore.append(["-"])
				for Proper in Data.Properties:
					self.liststore.append(list(Proper))

				# Associando a array (ListStore) ao ComboBox
				self.combo = self.builder.get_object('Grandeza')
				self.combo.set_model(self.liststore)

				# É necessário adicionar um renbderizador de texto ao ComboBox
				renderer_text = Gtk.CellRendererText()
				self.combo.pack_start(renderer_text, True)

				# Escolher qual coluna mostrar:
				self.combo.add_attribute(renderer_text, "text", 0)

				self.in_text = self.builder.get_object('in')
				self.out_text = self.builder.get_object('out')
				self.text = self.builder.get_object('textbox')

				# Opção ativa default
				self.combo.set_active(0)

				# Connect signals
				self.builder.connect_signals(self)

				# Everything is ready
				self.window.show()

		def on_window_destroy(self, widget):
				'''Classical window close button.'''
				Gtk.main_quit()

		def on_Button_pressed(self, button):
				global Data 
				Data = ReadExcel()

				self.liststore.clear()

				self.liststore.append(["-"])
				for Proper in Data.Properties:
					self.liststore.append(list(Proper))

				self.combo.clear()
				self.combo.set_model(self.liststore)

				renderer_text = Gtk.CellRendererText()
				self.combo.pack_start(renderer_text, True)
				self.combo.add_attribute(renderer_text, "text", 0)

				self.combo_Unit = self.builder.get_object('Unit_in')
				self.combo_Unit.clear()
				self.combo_Unit = self.builder.get_object('Unit_out')
				self.combo_Unit.clear()

				self.text.set_text("Dados carregados!")

		def on_combo_changed(self, widget):
				'''Verify which option is selected'''
				model = widget.get_model()
				self.active  = widget.get_active()
				if self.active  >= 0:
						code = model[self.active][0]
						self.text.set_text('Opção selecionada: {}'.format(code))
				else:
						self.text.set_text("Sem opção")

				#Calling UnitComboBox_Callback to sort new Units to IN COMBOBOX
				self.combo_Unit = self.builder.get_object('Unit_in')
				UnitComboBox_Callback(self, Data)
				renderer_text = Gtk.CellRendererText()
				self.combo_Unit.pack_start(renderer_text, True)
				self.combo_Unit.add_attribute(renderer_text, "text", 0)

				#Calling UnitComboBox_Callback to sort new Units to IN COMBOBOX
				self.combo_Unit = self.builder.get_object('Unit_out')
				UnitComboBox_Callback(self, Data)
				renderer_text = Gtk.CellRendererText()
				self.combo_Unit.pack_start(renderer_text, True)
				self.combo_Unit.add_attribute(renderer_text, "text", 0)


		def on_combo_changed_in(self, widget):
			self.active_in = widget.get_active()
			self.in_text.set_text(" ")
			self.out_text.set_text(" ")
			
		
		def on_combo_changed_out(self, widget):
			self.active_out = widget.get_active()
			self.in_text.set_text(" ")
			self.out_text.set_text(" ")


		def in_changed(self, widget):
			#Get objects from in and out boxes
			enter = self.in_text.get_text()

			try:		#If it's a number
				aux = float(enter) * Data.factors[self.active_in][self.active-1]/Data.factors[self.active_out][self.active-1]
				out = str(aux)
				self.out_text.set_text(out)
			except:
				if enter != " ":
					self.text.set_text("Entrada inválida! Coloque apenas números")
					return 0
			
			self.text.set_text(" ")
			
if __name__ == '__main__':
		try:
				gui = TheApp()
				Gtk.main()
		except KeyboardInterrupt:
				pass

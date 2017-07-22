from Tkinter import *
import random
from datetime import datetime

class RoutineGUI:

	routines = []
	selected_routine = ""
	date_pattern = "%d/%m/%Y"

	def __init__(self, master, routines):

		self.routines = routines

		self.master = master
		master.title("Routine Builder")

		self.label = Label(master, text = "Basic interface for Routine Builder Version 1")

		self.pick_routine_button = Button(master, text = "Pick new routine to run", command = self.pick_routine)

		self.label_text = StringVar()
		self.label_text.set("")
		self.output = Label(master, textvariable = self.label_text)

		self.add_routine_button = Button(master, text = "Add a new routine", command = self.add_routine)
		self.routine_entry_field = Entry(master)

		self.remove_routine_button = Button(master, text = "Remove a routine", command = self.remove_routine)

		self.OPTIONS = [row[0] for row in self.routines]
		self.removed = StringVar(self.master)
		self.removed.set(self.OPTIONS[0])
		self.removable_menu = apply(OptionMenu, (master, self.removed) + tuple(self.OPTIONS))

		self.exit_button = Button(master, text = "Exit", command = master.quit)

		self.label.grid(row = 0)
		self.pick_routine_button.grid(row = 1, column = 0, columnspan = 1)
		self.output.grid(row = 1, column = 1, columnspan = 2)
		self.add_routine_button.grid(row = 2, column = 0, columnspan = 1)
		self.routine_entry_field.grid(row = 2, column = 1, columnspan = 2)
		self.remove_routine_button.grid(row = 3, column = 0, columnspan = 1)
		self.removable_menu.grid(row = 3, column = 1, columnspan = 2)
		self.exit_button.grid(row = 4)

	def pick_routine(self):
		if(len(self.routines) != 0):
			self.selected_routine = self.routines[random.randrange(len(self.routines))][0]
		else:
			self.selected_routine = "Routines list empty. Please create new routines."
		print(self.selected_routine)
		self.label_text.set(self.selected_routine)

	def add_routine(self):
		new_routine = self.routine_entry_field.get()
		today_string = self.__convert_datetime_to_char(datetime.today())
		self.routines.append([new_routine, today_string])
		self.removable_menu['menu'].add_command(label = new_routine, command=lambda: self.removed.set(new_routine))
		print "Added '" + new_routine, "' to routines!"

	def remove_routine(self):

		self.routines = filter(lambda routine: not (routine[0] == self.removed.get()), self.routines)
		self.removable_menu['menu'].delete(self.removed.get())
		print "Removed '" + self.removed.get() + "' from routines!"

	def __convert_datetime_to_char(self, dt):
		return dt.strftime(self.date_pattern)

	def __convert_char_to_datetime(self, dt):
		return datetime.strptime(dt, self.date_pattern)

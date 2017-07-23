from Tkinter import *
import random
from datetime import datetime

class RoutineGUI:

	routines = []
	selected_routine = ""
	date_pattern = "%d/%m/%Y"
	empty_list_message = 'Routine list empty'

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

		self.PRIORITY = [1, 2, 3]
		self.level = StringVar(self.master)
		self.level.set(self.PRIORITY[0])
		self.priority_menu = apply(OptionMenu, (master, self.level) + tuple(self.PRIORITY))

		self.priority_label = Label(master, text = "Higher Priority # is more likely to be run.")

		self.remove_routine_button = Button(master, text = "Remove a routine", command = self.remove_routine)

		self.removed = StringVar(self.master)
		self.OPTIONS = [row[0] for row in self.routines]
		if len(self.OPTIONS) == 0:
			self.OPTIONS = ['Routine list empty']

		self.removed.set(self.OPTIONS[0])

		self.removable_menu = apply(OptionMenu, (master, self.removed) + tuple(self.OPTIONS))

		self.exit_button = Button(master, text = "Exit", command = master.quit)

		self.label.grid(row = 0)
		self.pick_routine_button.grid(row = 1, column = 0, columnspan = 1)
		self.output.grid(row = 1, column = 1, columnspan = 2)
		self.add_routine_button.grid(row = 2, column = 0, columnspan = 1)
		self.routine_entry_field.grid(row = 2, column = 1, columnspan = 2)
		self.priority_menu.grid(row = 2, column = 3, columnspan = 1)
		self.priority_label.grid(row = 3)
		self.remove_routine_button.grid(row = 4, column = 0, columnspan = 1)
		self.removable_menu.grid(row = 4, column = 1, columnspan = 2)
		self.exit_button.grid(row = 5)

	def pick_routine(self):
		if len(self.routines) != 0:
			self.select_random_routine_by_priority()
			self.update_runtime()
		else:
			self.selected_routine = "Routines list empty. Please create new routines."
		print(self.selected_routine)
		self.label_text.set(self.selected_routine)

	def select_random_routine_by_priority(self):

		random_list = []
		for routine in self.routines:
			for iter in range(0, int(routine[3])):
				random_list.append(routine[0])

		random_routine = random_list[random.randrange(len(random_list))]

		self.selected_routine = random_routine


	def update_runtime(self):
		for id, routine in enumerate(self.routines):
			if self.selected_routine in routine:
				last_run_string = self.__convert_datetime_to_char(datetime.today())
				self.routines[id] = [routine[0], routine[1], last_run_string, routine[3]]

	def add_routine(self):
		new_routine = self.routine_entry_field.get()
		new_priority = self.level.get()
		today_string = self.__convert_datetime_to_char(datetime.today())
		self.routines.append([new_routine, today_string,"", new_priority])
		self.removable_menu['menu'].add_command(label = new_routine, command=lambda: self.removed.set(new_routine))
		self.manage_empty_list_placeholder()
		print "Added '" + new_routine, "' to routines!"

	def remove_routine(self):

		self.routines = filter(lambda routine: not (routine[0] == self.removed.get()), self.routines)
		self.removable_menu['menu'].delete(self.removed.get())
		self.manage_empty_list_placeholder()
		print "Removed '" + self.removed.get() + "' from routines!"

	def manage_empty_list_placeholder(self):
		if len(self.routines) == 0:
			self.removable_menu['menu'].add_command(label =self.empty_list_message, command = lambda: self.removed.set(self.empty_list_message))
		else:
			try:
				self.removable_menu['menu'].delete(self.empty_list_message)
			except:
				print("No empty list message found.")

	def __convert_datetime_to_char(self, dt):
		return dt.strftime(self.date_pattern)

	def __convert_char_to_datetime(self, dt):
		return datetime.strptime(dt, self.date_pattern)

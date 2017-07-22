from Tkinter import *
import random

class RoutineGUI:

	routines = []
	selected_routine = ""

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
		self.remove_routine_button = Button(master, text = "Remove a routine", command = self.remove_routine)
		self.exit_button = Button(master, text = "Exit", command = master.quit)

		self.label.pack()
		self.pick_routine_button.pack()
		self.output.pack()
		self.add_routine_button.pack()
		self.remove_routine_button.pack()
		self.exit_button.pack()

	def pick_routine(self):
		if(len(self.routines) != 0):
			self.selected_routine = self.routines[random.randrange(len(self.routines))][0]
		else:
			self.selected_routine = "Routines list empty. Please create new routines."
		print(self.selected_routine)
		self.label_text.set(self.selected_routine)

	def add_routine(self):
		print("Do nothing for now")

	def remove_routine(self):
		print("Do nothing for now")
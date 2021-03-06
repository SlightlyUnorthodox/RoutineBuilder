from Tkinter import *
from RoutineGUI import RoutineGUI
import csv

class RoutineBuilder(object):

	routines_file = "routines.csv"
	routines_header = ['routine', 'created', ' last_run', 'priority']
	routines = []

	def __init__(self):

		self.__load_routines()

		self.root = Tk()
		self.routine_gui = RoutineGUI(self.root, self.routines)

	def start(self):

		self.root.mainloop()
		self.root.destroy()

		self.__update_routines(self.routine_gui.routines)

	def __load_routines(self):

		with open(self.routines_file, 'rb') as file:
			reader = csv.reader(file)
			next(reader, None)
			for row in reader:
				self.routines.append(row)

	def __update_routines(self, updated_routines):

		with open(self.routines_file, 'wb') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(self.routines_header)
			for row in updated_routines:
				writer.writerow(row)

if __name__ == "__main__":
	builder = RoutineBuilder()
	builder.start()
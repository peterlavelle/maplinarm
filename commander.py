#!/usr/bin/env python
import sys
import time
import os
import csv

#Add current directory to system path
sys.path.append(os.getcwd())

#import the maplinrobot class
from maplinrobot import MaplinRobot

class RobotCommander():
	def __init__(self):
		self.csvfile=''
		self.commands=''


	def ParseArguments(self):
		try:
			if len(sys.argv) > 1: # Valid number of arguments
				self.csvfile=str(sys.argv[1])
				return True
			else:
				return False
		except IndexError:
			print "None or wrong number of arguments supplied!\n"
			return False

	def CheckFileExists(self):
		if os.path.isfile(self.csvfile) and os.path.exists(self.csvfile):
			return True
		else:
			return False

	def ReadCSVFile(self):
		try:
			if self.ParseArguments() and self.CheckFileExists():
				self.commands = csv.reader(open(self.csvfile), delimiter=',')
				return True
			else:
				return False
		except csv.Error:
			print "Unable to load csv file\n"
			return False

	def RunCommands(self):
		try:
			r = MaplinRobot()
			if self.ReadCSVFile():
				for row in self.commands:
					print "Running command '%s' for a duration of %f second(s) with a pause of %f second(s)" %(str(row[0]), float(row[1]), float(row[2]))
					if r.MoveArm(t=float(row[1]), cmd=str(row[0])):
						time.sleep(float(row[2]))
					else:
						print "Problem sending commands. Exiting\n"
						return False

				#All commands done. Stop the arm
				print "\nAll commands executed. Stopping the arm\n"
				r.StopArm()
				return True
			else:
				print "Something went wrong!\n"
				r.StopArm()
				return False

		except KeyboardInterrupt:
			print "ctrl-c pressed. Exiting\n"
			#r.StopArm()
			return False


r = RobotCommander()
r.ParseArguments()
r.RunCommands()






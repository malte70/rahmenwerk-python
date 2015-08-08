#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2014-2015 Malte Bublitz
# All rights reserved.
# See COPYING.md for details.
#

import sys
try:
	from CLIApp.ansiconsole import *
	from CLIApp.app import *
	
except ImportError:
	print("CLIApp not found!")
	sys.exit(1)
	
class HelloWorldApp(CLIApp):
	_APP_NAME_    = "Python App Skeleton Demo: Hello World"
	_APP_VERSION_ = "0.1"
	
	def action_default(self, isDirect=True):
		if "--help" in self._options or "-h" in self._options:
			self.action_help()
			sys.exit(0)
		elif "--version" in self._options or "-V" in self._options:
			self.action_version()
			sys.exit(0)
		else:
			self.action_greet()
		
	def action_version(self):
		self.c.writeln(self._APP_NAME_ + " " + self._APP_VERSION_)
		
	def action_help(self):
		self.action_version()
		self.c.writeln("Usage:")
		self.c.writeln("\thello_world [--version|--help]")
		self.c.writeln("\thello_world [--name=Your Name]")
		self.c.writeln("Options:")
		self.c.writeln("\t--version  Show the version and exit")
		self.c.writeln("\t--help     Show the help and exit")
		self.c.writeln("\t--name     Set a name to greet")
		self.c.writeln("")
		
	def action_greet(self):
		GREET_NAME="World"
		for opt in self._options:
			if opt.startswith("--name="):
				GREET_NAME = opt[7:]
		
		self.c.writeln("Hello, "+GREET_NAME+"!")
		

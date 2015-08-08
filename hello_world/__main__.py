#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2014-2015 Malte Bublitz
# All rights reserved.
# See COPYING.md for details.
#

try:
	import App
except ImportError:
	import hello_world.App as App
	
def main():
	app = App.HelloWorldApp()
	app.run()
	
if __name__ == "__main__":
	main()


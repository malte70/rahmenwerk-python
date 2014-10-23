#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
# 

from distutils.core import setup

setup(
		name         = "hello-world",
		version      = "0.1",
		description  = "A simple hello world application",
		author       = "Malte Bublitz",
		author_email = "malte70@mcbx.de",
		url          = "https://malte-bublitz.de/hello-world",
		license      = "License :: OSI Approved :: BSD License",
		packages     = ["hello_world"],
		scripts      = ["bin/hello_world"]
	)


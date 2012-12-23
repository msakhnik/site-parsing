#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       безіменний.py
#       
#       Copyright 2012 morwin <morwin@morwin-HP-620>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       

import os
import os.path
import getpass
import sys

import auth

def main(address, password):
	auth.DoAuth(address, password)
	return 0

if len(sys.argv) != 3:
   print "Usage: %s address password" % sys.argv[0]
   sys.exit(1)

address = sys.argv[1]
password = sys.argv[2]

if __name__ == '__main__':
	main(address, password)

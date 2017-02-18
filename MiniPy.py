from math import *
from random import *
import re
import sublime, sublime_plugin

import sys 
import os
 # arrow-dists is the folder in our plugin
sys.path.append(os.path.join(os.path.dirname(__file__), "arrow"))
import arrow


def ts_precision():
    return 1000.0


def t(phrase, tz='-0000'):
    try:
        timestamp = int(phrase)
        return timestamp_to_string(timestamp, tz)
    except ValueError:
        return string_to_timestamp(phrase)


def timestamp_to_string(timestamp, tz_offset):
    fmt = 'YYYY-MM-DDTHH:mm:ss.SSSZ'
    # convert timezone offset to ISO with ':' (we dont use it)
    if ':' not in tz_offset:
        tz_offset = ':'.join([tz_offset[0:3], tz_offset[3:5]])
    return arrow.get(timestamp/ts_precision()).to(tz_offset).format(fmt)
        

def string_to_timestamp(string):
    return int(arrow.get(string).float_timestamp * ts_precision())


# reverse() in python3 
def rev(s): return s[::-1]


class Minipy_evalCommand(sublime_plugin.TextCommand):
	def run(self, edit, user_input=None):
		self.edit = edit
		view = self.view
		script = ""

		# sum the total number of special char $
		total = 0
		for region in view.sel():
			total += view.substr(region).count("$")

		### print("total = ", total)
		# build a list from 1 to the number of special chars
		serial_number = list(range(1, total+1))
		# serial_number.reverse()
		serial_number = rev(serial_number)
		### print(repr(serial_number))

		# replace each special char $ with the next index from serial_number list
		# and eval the expression
		for region in view.sel():
			if region.begin() != region.end():
				script = view.substr(region)
				for n in range(script.count("$")):
					script = re.sub(r"\$", str(serial_number.pop()), script, 1)
				# print(eval(script))
				view.replace(edit, region, str(eval(script)))

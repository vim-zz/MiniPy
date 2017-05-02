from math import *
from random import *
import re
import sublime
import sublime_plugin

# reverse() in python3


def rev(s):
    return s[::-1]


class Minipy_evalCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.edit = edit
        view = self.view
        script = ""

        # sum the total number of special char $
        total = 0
        for region in view.sel():
            total += view.substr(region).count("$")

        print("total = ", total)
        # build a list from 1 to the number of special chars
        serial_number = list(range(1, total + 1))
        # serial_number.reverse()
        serial_number = rev(serial_number)
        print(repr(serial_number))

        # replace each special char $ with the next index from serial_number list
        # and eval the expression
        for region in view.sel():
            if region.begin() != region.end():
                script = view.substr(region)
                for n in range(script.count("$")):
                    script = re.sub(r"\$", str(serial_number.pop()), script, 1)
                # print(eval(script))
                view.replace(edit, region, str(eval(script)))

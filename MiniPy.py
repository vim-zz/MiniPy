from math import *
from random import *
from hashlib import md5 as _md5
from hashlib import sha1 as _sha1
from collections import Counter
from dateutil import tz
import datetime
import re
import sublime
import sublime_plugin


def cumsum(lst):
    return [sum(lst[:i]) for i in range(1, len(lst)+1)]


def cumprod(lst, use_logsum=False):
    def do_cumprod(lst):
        tmp = 1
        toReturn = list()
        for el in lst:
            tmp *= el
            toReturn.append(tmp)
        return toReturn

    if use_logsum:
        return [exp(el_log) for el_log in cumsum([log(el) for el in lst])]
    else:
        return do_cumprod(lst)


def dnow():
    return datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y')


def tnow():
    return datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')


def dtnow():
    return datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S')


def _hashfunc(hashfunc, obj):
    s = str(obj)
    h = hashfunc(s.encode('utf-8'))
    return h.hexdigest()


def md5(obj):
    return _hashfunc(_md5, obj)


def sha1(obj):
    return _hashfunc(_sha1, obj)


def set_intersect(itr0, itr1):
    s0, s1 = set(itr0), set(itr1)
    return s0.intersection(s1)


def set_difference(itr0, itr1):
    s0, s1 = set(itr0), set(itr1)
    return s0 - s1


def set_symdiff(itr0, itr1):
    s0, s1 = set(itr0), set(itr1)
    return s0.symmetric_difference(s1)


def formatnum(num, digits=8, scientificNotation=None):

    def normalFormatting(num, digits):
        return ('{:.%df}' % digits).format(num)

    def scientificFormatting(num, digits):
        return ('{:.%de}' % digits).format(num)

    if scientificNotation is False:
        return normalFormatting(num, digits)

    if scientificNotation is True:
        return scientificFormatting(num, digits)

    if scientificNotation is None:
        scientificNotation = 8

    if isinstance(scientificNotation, int):
        if len(normalFormatting(num, digits)) > scientificNotation:
            return scientificFormatting(num, digits)
        return normalFormatting(num, digits)


# reverse() in python3
def rev(s):
    return s[::-1]


# timestamp (unix time since epoch) to string
def ts(timestamp_sec, fmt='%Y-%m-%dT%H:%M:%S.%f%z'):
    tzinfo = tz.tzutc()
    return datetime.datetime.utcfromtimestamp( timestamp_sec ).replace(tzinfo=tzinfo).strftime( fmt )


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

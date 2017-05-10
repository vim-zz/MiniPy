# MiniPy

Sublime Text 3 plugin - inline python evaluation.

## Functionality

### As a calculator

For example you can write 3.14*0.6 and get the result (1.884) in your text.
It also supports multiple selection.

### Incremnt counter at cursor positions

Another feature is the use of $ as accumolation variable, e.g. having the following multipe selection:

	arr[$]
	arr[$]
	arr[$]

will result with

	arr[1]
	arr[2]
	arr[3]

similarly:

	arr[0 ]      arr[0]
	arr[$+2]  -> arr[3]
	arr[$*3]     arr[6]

### General Python evalueator

Besides that, you have the following imports avaiable:

	from math import *
	from random import *
	from collections import Counter
	import datetime
	import re  # though you should probably use the build in regex features of ST instead.

So you can do:

	Counter(('Ann', 'Bob', 'Bob', 'Michael'))                                     -> Counter({'Bob': 2, 'Ann': 1, 'Michael': 1})
	Counter(('Ann', 'Bob', 'Bob', 'Michael', 'michael'))                          -> Counter({'Bob': 2, 'Ann': 1, 'michael': 1, 'Michael': 1})
	Counter(name.title() for name in ('Ann', 'Bob', 'Bob', 'Michael', 'michael')) -> Counter({'Bob': 2, 'Michael': 2, 'Ann': 1})

### Computing checksums

And the functions `md5` and `sha1` returns the correspondingly hex-digest of the stringified version of the inputs, e.g. `md5(['foo', 'bar', 'baz']) = dbb432a3f0ac1a2687911715dfbf7502`. Notice that it's possible to hash the list _because it's the string-representation of the list which are being hashed!_

The python `hashlib.md5` and `hashlib.sha1` functions are avaiable under the names `_md5` and `_sha1`.

### Inserting datatimes

The functions `dnow`, `tnow` and `dtnow` return respectively the current string-formatted date, time and datetime:

	dnow()  -> 03/05/2017
	tnow()  -> 09:36:03
	dtnow() -> 03/05/2017 09:36:03

Notice that you need to have parenthesis after the function name to invoke the function call.


### Computing with sets

While you can just use the regular python to do set computations, there's a few functions included for convinience: `set_intersect`, `set_difference` and `set_symdiff`.

The functions takes two iterable arguments, which are turned into sets, and the computations are performed:

	set_intersect('foo bar', 'foo baz')  -> {'b', 'a', ' ', 'o', 'f'}
	set_intersect('foo baz', 'foo bar')  -> {'b', 'a', ' ', 'o', 'f'}
	set_difference('foo baz', 'foo bar') -> {'z'}
	set_difference('foo bar', 'foo baz') -> {'r'}
	set_symdiff('foo baz', 'foo bar')    -> {'z', 'r'}
	set_symdiff('foo bar', 'foo baz')    -> {'z', 'r'}


### Computing cumultative sums and products

Compute the cumultative sum of an iterable:

	cumsum([1,2,3,4,5]) -> [1, 3, 6, 10, 15]
	cumsum([0.02809, 0.05619, 0.08646, 0.11919, 0.15192, 0.18465, 1.31694]) -> [0.02809, 0.08428, 0.17074, 0.28993, 0.44185, 0.6265000000000001, 1.94344]

And a cumultative product

	cumprod([1, 2, 3, 4, 5]) -> [1, 2, 6, 24, 120]
	cumprod([0.02809, 0.05619, 0.08646, 0.11919, 0.15192, 0.18465, 1.31694]) -> [0.02809, 0.0015783771, 0.000136466484066, 1.626544023582654e-05, 2.471045680626768e-06, 4.5627858492773275e-07, 6.008915196347284e-07]

But doing products of a lot of small numbers are prone to errors, so we can use a math trick: $\exp \left[ \sum \log \left[ A \right] \right] = \prod A$

	cumprod([1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14]) -> [1e-08, 1e-17, 1e-27, 1e-38, 9.999999999999999e-51, 9.999999999999999e-64, 1e-77]
	cumprod([1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14], use_logsum=True) -> [9.999999999999982e-09, 9.99999999999999e-18, 1.0000000000000022e-27, 9.999999999999936e-39, 9.999999999999944e-51, 1.0000000000000049e-63, 9.999999999999967e-78]
	cumprod([1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14], use_logsum=True) -> # same result as above.


### Formatting numbers

The fnuction `formatnum` formats numbers, and takes two mandatory and an optional argument:

num
:	The number bieng formatted.

digits
:	The number of desired digits in the formatted number.

scientificNotation
:	Wether of not to use scientific notation.
:	Can be True, False or int, where int is the threshold for how many characters the number may contain when formatted un-scientifically, before switching to scientific notation.
:	This is the default behaviour, and it's set to 8.

Example usage:

	formatnum(0.123456789, 4)                -> 0.1235
	formatnum(0.123456789, 9)                -> 1.234567890e-01
	formatnum(123456789.0, 9)                -> 1.234567890e+08
	formatnum(123456789.0, 2)                -> 1.23e+08
	formatnum(123.456789, 12)                -> 1.234567890000e+02
	formatnum(123.456789, 12, False)         -> 123.456789000000
	formatnum(123.456789, 3)                 -> 123.457
	formatnum(3.14159, 4)                    -> 3.1416
	formatnum(3.14159, 3)                    -> 3.142
	formatnum(3.14159, 2)                    -> 3.14
	formatnum(3.14159, 2, True)              -> 3.14e+00
	formatnum(3.141592653589793238462643, 3) -> 3.142


## Usage

To evaluate term, highlight and:

	Super + Shift + X for Mac OS X
	Ctrl + Shift + X for Windows/Linux

# MiniPy

Sublime Text 3 plugin - inline python evaluation.

For example you can write 3.14*0.6 and get the result (1.884) in your text.
It also supports multiple selection.

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

## Usage

To evaluate term, highlight and:

	Super + Shift + X for Mac OS X
	Ctrl + Shift + X for Windows/Linux

# MiniPy

Sublime Text 3 plugin - inline python evaluation.

For example you can write `3.14*0.6` and get the result `1.884` right in your open view.

Multiple selection is supported as well.

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

## Time

The Arrow library is used to evaluate epoch timestamps to strings and vice versa.

To use just wrap your text with `t()`, for example:

	t(1444321015000) -> 2015-10-08T16:16:55.000-0000
	t('2015-10-08T16:16:55.000-0000') -> 1444321015000
	# with timezone UTC+6
	t('2016-02-16T20:14:03.834+0600') -> 1444321015000

## Usage

To evaluate term, highlight and:

	Super + Shift + X for Mac OS X
	Ctrl + Shift + X for Windows/Linux

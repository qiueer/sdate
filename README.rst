simple datetime
===============

A library that we can get datetime simply and easily

Installation
------------

Install using pip::

    pip install sdate
    
Install using source code::

	git clone https://github.com/qiueer/sdate
	cd sdate
	python setup.py install


Usage
-----

Run commands as you would in bash::

    >>> from sdate import sdate
    >>> sdate()
    cmds.pyc

Chain commands for the same effect::

    >>> cmds('ls . ').cmds('grep ".pyc"')
    cmds.pyc

Support + Contributing
----------------------

Feel free to make pull requests, or report issues via the repo:

https://github.com/qiueer/sdate

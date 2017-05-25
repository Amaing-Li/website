#!/usr/bin/env python

import sys
import os


def main():
    if len(sys.argv) > 1 and sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]] > index.html".format(sys.argv[0]))
        sys.exit()

    print_start()
    print_line()
    print_end()


def print_start():
    print("""
    <!DOCTYPE html>
    <html>
	    <head>
		    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    	</head>
	    <body>
		    <h1>Welcome!</h1>
		    <p>I hope that you can benefit from what I share.</p>
    """)


def print_line():
    for name in os.listdir("."):
        if name not in {"index.html", "csv2html.py"}:
            print("                    <h2><a href={0}>{0}</a></h2>".format(name))


def print_end():
    print("""\
    	</body>
    </html>
    """)


main()

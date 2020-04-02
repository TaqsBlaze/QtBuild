
from distutils.core import setup
import py2exe,os,sys
includes=["sys","os","PyQt5"]
excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
            "pywin.dialogs", "pywin.dialogs.list", "win32com.server","numpy",
			"tcl",4
			]

options = {
    "bundle_files": 1, # create singlefile exe
	"compressed": 1, # compress the library archive
	"excludes": excludes,
	"includes": includes,
	"dll_excludes": ["w9xpopen.exe"] # we don't need this
	}

setup(
	options = {"py2exe": options},
	zipfile = None, # append zip-archive to the executable.
	version = "1.0",
	description = "SOFTAZ Software",
	console = {"script":"QtBuilder.py"}
	)

from cx_Freeze import setup, Executable

buildOptions = dict(
	includes = 'calcGui.py'
)

setup(
	name="Grade Calculator ",
	  version = "0.1",
	  description = "Calculator for grade point average and final grade",
	  author = "Justice Jacobs",
	  executables = [Executable("main.py")]
)

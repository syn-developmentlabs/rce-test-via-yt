from distutils.core import setup
import py2exe

setup(
    py_modules=['main'],  # Explicitly list the module you want to convert
    console=['main.py'],  # Include your main script file explicitly
)

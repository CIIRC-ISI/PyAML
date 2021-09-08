"""
Python preamble
This script serves to create the context in which all python expressions in the AutomationML document will be evaluated.
By default only python builtins are available.
All imports, variable definitions, function definitions etc. go here.
"""

from time import ctime

configuration = 1


def add2(number):
    return number + 2
